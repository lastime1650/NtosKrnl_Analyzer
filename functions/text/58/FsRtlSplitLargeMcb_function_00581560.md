# FsRtlSplitLargeMcb

- RVA: `0x00581560`–`0x005815B4` (길이 `84` bytes)
- VA: `0x0000000140581560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5D38`
- 디코드: `25`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00581580` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00581590` → [FsRtlSplitBaseMcb](FsRtlSplitBaseMcb_function_005813E0.md) (function, `0x005813E0`)
- `0x0058159B` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581560  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00581565  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0058156A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0058156F  57                              push rdi
00581570  48 83 EC 20                     sub rsp, 0x20
00581574  49 8B F8                        mov rdi, r8
00581577  48 8B F2                        mov rsi, rdx
0058157A  48 8B D9                        mov rbx, rcx
0058157D  48 8B 09                        mov rcx, qword ptr [rcx]
00581580  E8 1B D0 C8 FF                  call 0x14020e5a0
00581585  90                              nop
00581586  48 8D 4B 08                     lea rcx, [rbx + 8]
0058158A  4C 8B C7                        mov r8, rdi
0058158D  48 8B D6                        mov rdx, rsi
00581590  E8 4B FE FF FF                  call 0x1405813e0
00581595  40 8A F8                        mov dil, al
00581598  48 8B 0B                        mov rcx, qword ptr [rbx]
0058159B  E8 20 04 CD FF                  call 0x1402519c0
005815A0  40 8A C7                        mov al, dil
005815A3  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
005815A8  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
005815AD  48 83 C4 20                     add rsp, 0x20
005815B1  5F                              pop rdi
005815B2  C3                              ret
005815B3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlSplitLargeMcb(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireFastMutex(*(unsigned __int64 *)(a1), a2, a3, a4);
    result = FsRtlSplitBaseMcb(a1 + 8, a2, a3, a4);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(a1), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)((unsigned __int8)(result));
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlSplitLargeMcb(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireFastMutex(*(uint64_t *)(arg1), Arg2, Arg3, a4);
    result = FsRtlSplitBaseMcb(Arg1 + 8, Arg2, Arg3, a4);
    result = ExReleaseFastMutex(*(uint64_t *)(arg1), Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)((uint8_t)(result));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581560[BB_00581560]
  bb_005815B3[BB_005815B3]
```
