# RtlTimeToSecondsSince1980

- RVA: `0x00457B70`–`0x00457BAA` (길이 `58` bytes)
- VA: `0x0000000140457B70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `18`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00457B84` → [RtlExtendedMagicDivide](RtlExtendedMagicDivide_function_00457BF0.md) (function, `0x00457BF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00457B7A` → RVA `0x00014D30` (`.rdata`; read)
- `0x00457B89` → RVA `0x00014D20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00457B70  48 83 EC 28                     sub rsp, 0x28
00457B74  48 8B 09                        mov rcx, qword ptr [rcx]
00457B77  4C 8B D2                        mov r10, rdx
00457B7A  48 8B 15 AF D1 BB FF            mov rdx, qword ptr [rip - 0x442e51]
00457B81  41 B0 17                        mov r8b, 0x17
00457B84  E8 67 00 00 00                  call 0x140457bf0
00457B89  48 2B 05 90 D1 BB FF            sub rax, qword ptr [rip - 0x442e70]
00457B90  48 8B C8                        mov rcx, rax
00457B93  48 C1 E9 20                     shr rcx, 0x20
00457B97  85 C9                           test ecx, ecx
00457B99  75 0B                           jne 0x140457ba6
00457B9B  41 89 02                        mov dword ptr [r10], eax
00457B9E  B0 01                           mov al, 1
00457BA0  48 83 C4 28                     add rsp, 0x28
00457BA4  C3                              ret
00457BA5  CC                              int3
00457BA6  32 C0                           xor al, al
00457BA8  EB F6                           jmp 0x140457ba0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlTimeToSecondsSince1980(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlExtendedMagicDivide(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(v_rip - 4468305), 23, a4);
    result = (result) - (*(unsigned __int64 *)(v_rip - 4468336));
    a1 = (result) >> (32);
    if ((unsigned int)(a1) != 0) goto loc_00457BA6;
    *(unsigned int *)(a2) = (unsigned int)(result);
loc_00457BA0:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_00457BA6:
    result = 0;
    goto loc_00457BA0;
}
```

## 5. (Beta) C Style

```c
int64_t RtlTimeToSecondsSince1980(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlExtendedMagicDivide(*(uint64_t *)(arg1), *(uint64_t *)(v_rip - 0x442E51), 23, a4);
    result = (result) - (*(uint64_t *)(v_rip - 0x442E70));
    Arg1 = (result) >> (32);
    if ((uint32_t)(Arg1) != 0) goto loc_00457BA6;
    *(uint32_t *)(Arg2) = (uint32_t)(result);
loc_00457BA0:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_00457BA6:
    result = 0;
    goto loc_00457BA0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00457B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00457B70[BB_00457B70]
  bb_00457B9B[BB_00457B9B]
  bb_00457BA0[BB_00457BA0]
  bb_00457BA5[BB_00457BA5]
  bb_00457BA6[BB_00457BA6]
  bb_00457B70 -->|branch| bb_00457BA6
  bb_00457B70 -->|fallthrough| bb_00457B9B
  bb_00457B9B -->|flow| bb_00457BA0
  bb_00457BA5 -->|flow| bb_00457BA6
  bb_00457BA6 -->|branch| bb_00457BA0
```
