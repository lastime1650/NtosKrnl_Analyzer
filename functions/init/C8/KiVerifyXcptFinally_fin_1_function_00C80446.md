# KiVerifyXcptFinally$fin$1

- RVA: `0x00C80446`–`0x00C80482` (길이 `60` bytes)
- VA: `0x0000000140C80446`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `19`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C80475` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C8046A` → RVA `0x00C3AE1B` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C80475` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C80446  40 55                           push rbp
00C80448  48 83 EC 20                     sub rsp, 0x20
00C8044C  48 8B EA                        mov rbp, rdx
00C8044F  0F B6 C1                        movzx eax, cl
00C80452  84 C9                           test cl, cl
00C80454  74 25                           je 0x140c8047b
00C80456  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00C8045A  83 78 0C 00                     cmp dword ptr [rax + 0xc], 0
00C8045E  7E 1B                           jle 0x140c8047b
00C80460  69 40 0C C9 41 6A 29            imul eax, dword ptr [rax + 0xc], 0x296a41c9
00C80467  89 45 24                        mov dword ptr [rbp + 0x24], eax
00C8046A  48 8D 15 AA A9 FB FF            lea rdx, [rip - 0x45656]
00C80471  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00C80475  E8 C6 F6 87 FF                  call 0x1404ffb40
00C8047A  90                              nop
00C8047B  48 83 C4 20                     add rsp, 0x20
00C8047F  5D                              pop rbp
00C80480  C3                              ret
00C80481  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcptFinally_fin_1(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 == 0) goto loc_00C8047B;
    result = *(unsigned __int64 *)(a2 + 64);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12)) >= = 0) {
        result = (unsigned int)((*(unsigned __int64 *)(a2 + 64)) * (*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12)));
        *(unsigned int *)(a2 + 36) = (unsigned int)(result);
        a2 = v_rip - 284246;
        a1 = *(unsigned __int64 *)(a2 + 40);
        result = local_unwind(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcptFinally_fin_1(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 == 0) goto loc_00C8047B;
    result = *(uint64_t *)(arg2 + 0x40);
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC)) >= = 0) {
        result = (uint32_t)((*(uint64_t *)(arg2 + 0x40)) * (*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC)));
        *(uint32_t *)(arg2 + 0x24) = (uint32_t)(result);
        Arg2 = v_rip - 284246;
        Arg1 = *(uint64_t *)(arg2 + 0x28);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C80446&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C80446[BB_00C80446]
  bb_00C80456[BB_00C80456]
  bb_00C80460[BB_00C80460]
  bb_00C8047B[BB_00C8047B]
  bb_00C80481[BB_00C80481]
  bb_00C80446 -->|branch| bb_00C8047B
  bb_00C80446 -->|fallthrough| bb_00C80456
  bb_00C80456 -->|branch| bb_00C8047B
  bb_00C80456 -->|fallthrough| bb_00C80460
  bb_00C80460 -->|flow| bb_00C8047B
```
