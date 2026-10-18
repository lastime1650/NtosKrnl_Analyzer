# RawQueryFsVolumeInfo

- RVA: `0x009A4510`–`0x009A457F` (길이 `111` bytes)
- VA: `0x00000001409A4510`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069AD0`
- 디코드: `33`개 명령, `111/111` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A4530` → [RawBeginOperation](../../text/41/RawBeginOperation_function_00411F10.md) (function, `0x00411F10`)
- `0x009A455B` → [RawEndOperation](../../text/48/RawEndOperation_function_0048E70C.md) (function, `0x0048E70C`)

### Direct callers
- [RawQueryVolumeInformation](RawQueryVolumeInformation_function_009A4414.md) at `0x009A444B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009A4530` → [RawBeginOperation](../../text/41/RawBeginOperation_function_00411F10.md) (`PAGE` → `.text`)
  - `0x009A455B` → [RawEndOperation](../../text/48/RawEndOperation_function_0048E70C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A4510  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009A4515  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
009A451A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
009A451F  57                              push rdi
009A4520  48 83 EC 20                     sub rsp, 0x20
009A4524  49 8B F1                        mov rsi, r9
009A4527  49 8B D8                        mov rbx, r8
009A452A  48 8B EA                        mov rbp, rdx
009A452D  48 8B F9                        mov rdi, rcx
009A4530  E8 DB D9 A6 FF                  call 0x140411f10
009A4535  84 C0                           test al, al
009A4537  74 3F                           je 0x1409a4578
009A4539  83 06 EE                        add dword ptr [rsi], -0x12
009A453C  33 C0                           xor eax, eax
009A453E  0F 57 C0                        xorps xmm0, xmm0
009A4541  48 8B D5                        mov rdx, rbp
009A4544  0F 11 03                        movups xmmword ptr [rbx], xmm0
009A4547  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
009A454B  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
009A4552  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
009A4555  89 4B 08                        mov dword ptr [rbx + 8], ecx
009A4558  48 8B CF                        mov rcx, rdi
009A455B  E8 AC A1 AE FF                  call 0x14048e70c
009A4560  33 C0                           xor eax, eax
009A4562  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009A4567  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
009A456C  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
009A4571  48 83 C4 20                     add rsp, 0x20
009A4575  5F                              pop rdi
009A4576  C3                              ret
009A4577  CC                              int3
009A4578  B8 6E 02 00 C0                  mov eax, 0xc000026e
009A457D  EB E3                           jmp 0x1409a4562
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RawQueryFsVolumeInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = RawBeginOperation(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009A4578;
    result = 0;
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = 0;
    *(unsigned int *)(a3 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 200) + 24)));
    result = RawEndOperation(a1, a2, a3, a4);
    result = 0;
loc_009A4562:
    v_rsp = (v_rsp) + (32);
    return result;
loc_009A4578:
    goto loc_009A4562;
}
```

## 5. (Beta) C Style

```c
int64_t RawQueryFsVolumeInfo(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = RawBeginOperation(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009A4578;
    result = 0;
    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = 0;
    *(uint32_t *)(arg3 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xC8) + 0x18)));
    result = RawEndOperation(Arg1, Arg2, Arg3, Arg4);
    result = 0;
loc_009A4562:
    local_rsp = (local_rsp) + (32);
    return result;
loc_009A4578:
    goto loc_009A4562;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x8` | `32` | `W` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A4510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A4510[BB_009A4510]
  bb_009A4539[BB_009A4539]
  bb_009A4562[BB_009A4562]
  bb_009A4577[BB_009A4577]
  bb_009A4578[BB_009A4578]
  bb_009A4510 -->|branch| bb_009A4578
  bb_009A4510 -->|fallthrough| bb_009A4539
  bb_009A4539 -->|flow| bb_009A4562
  bb_009A4577 -->|flow| bb_009A4578
  bb_009A4578 -->|branch| bb_009A4562
```
