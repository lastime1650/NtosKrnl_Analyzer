# PsDereferenceKernelStack

- RVA: `0x00AA3630`–`0x00AA3666` (길이 `54` bytes)
- VA: `0x0000000140AA3630`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068804`
- 디코드: `16`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA365A` → [KeEnumerateKernelStackSegments](../../text/2A/KeEnumerateKernelStackSegments_function_002A13B8.md) (function, `0x002A13B8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AA3653` → RVA `0x002A1550` (`PspDeleteKernelStack`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AA365A` → [KeEnumerateKernelStackSegments](../../text/2A/KeEnumerateKernelStackSegments_function_002A13B8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA3630  40 53                           push rbx
00AA3632  48 83 EC 20                     sub rsp, 0x20
00AA3636  48 8B D9                        mov rbx, rcx
00AA3639  83 C8 FF                        or eax, 0xffffffff
00AA363C  F0 0F C1 81 EC 05 00 00         lock xadd dword ptr [rcx + 0x5ec], eax
00AA3644  83 F8 01                        cmp eax, 1
00AA3647  74 07                           je 0x140aa3650
00AA3649  48 83 C4 20                     add rsp, 0x20
00AA364D  5B                              pop rbx
00AA364E  C3                              ret
00AA364F  CC                              int3
00AA3650  45 33 C0                        xor r8d, r8d
00AA3653  48 8D 15 F6 DE 7F FF            lea rdx, [rip - 0x80210a]
00AA365A  E8 59 DD 7F FF                  call 0x1402a13b8
00AA365F  48 83 63 28 00                  and qword ptr [rbx + 0x28], 0
00AA3664  EB E3                           jmp 0x140aa3649
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsDereferenceKernelStack(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) goto loc_00AA3650;
loc_00AA3649:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AA3650:
    a3 = 0;
    result = KeEnumerateKernelStackSegments(a1, v_rip - 8397066, a3, a4);
    goto loc_00AA3649;
}
```

## 5. (Beta) C Style

```c
int64_t PsDereferenceKernelStack(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) goto loc_00AA3650;
loc_00AA3649:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AA3650:
    Arg3 = 0;
    result = KeEnumerateKernelStackSegments(Arg1, v_rip - 8397066, Arg3, a4);
    goto loc_00AA3649;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x5EC` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA3630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA3630[BB_00AA3630]
  bb_00AA3649[BB_00AA3649]
  bb_00AA364F[BB_00AA364F]
  bb_00AA3650[BB_00AA3650]
  bb_00AA3630 -->|branch| bb_00AA3650
  bb_00AA3630 -->|fallthrough| bb_00AA3649
  bb_00AA364F -->|flow| bb_00AA3650
  bb_00AA3650 -->|branch| bb_00AA3649
```
