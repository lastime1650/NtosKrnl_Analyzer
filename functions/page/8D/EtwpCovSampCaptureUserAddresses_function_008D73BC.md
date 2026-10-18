# EtwpCovSampCaptureUserAddresses

- RVA: `0x008D73BC`–`0x008D741F` (길이 `99` bytes)
- VA: `0x00000001408D73BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069AD0`
- 디코드: `29`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008D73D6` → [EtwpCovSampCaptureBufferGet](../../text/43/EtwpCovSampCaptureBufferGet_function_0043C1A0.md) (function, `0x0043C1A0`)
- `0x008D73EB` → [EtwpCovSampCaptureBufferAddIP](../../text/46/EtwpCovSampCaptureBufferAddIP_function_00463F80.md) (function, `0x00463F80`)
- `0x008D73F0` → [EtwpCovSampCaptureUserStack](EtwpCovSampCaptureUserStack_function_008D78A4.md) (function, `0x008D78A4`)
- `0x008D73FB` → [EtwpCovSampCaptureBufferMapAddressesAndQueue](EtwpCovSampCaptureBufferMapAddressesAndQueue_function_008D7430.md) (function, `0x008D7430`)

### Direct callers
- [EtwpCovSampCaptureApc](../../text/44/EtwpCovSampCaptureApc_function_004440D0.md) at `0x004441AF`
- [EtwpCovSampCaptureSample](../../text/65/EtwpCovSampCaptureSample_function_00653F24.md) at `0x00654082`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008D73D6` → [EtwpCovSampCaptureBufferGet](../../text/43/EtwpCovSampCaptureBufferGet_function_0043C1A0.md) (`PAGE` → `.text`)
  - `0x008D73EB` → [EtwpCovSampCaptureBufferAddIP](../../text/46/EtwpCovSampCaptureBufferAddIP_function_00463F80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D73BC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008D73C1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
008D73C6  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008D73CB  57                              push rdi
008D73CC  48 83 EC 20                     sub rsp, 0x20
008D73D0  48 8B EA                        mov rbp, rdx
008D73D3  48 8B F1                        mov rsi, rcx
008D73D6  E8 C5 4D B6 FF                  call 0x14043c1a0
008D73DB  33 DB                           xor ebx, ebx
008D73DD  48 8B F8                        mov rdi, rax
008D73E0  48 85 C0                        test rax, rax
008D73E3  74 33                           je 0x1408d7418
008D73E5  48 8B D5                        mov rdx, rbp
008D73E8  48 8B C8                        mov rcx, rax
008D73EB  E8 90 CB B8 FF                  call 0x140463f80
008D73F0  E8 AF 04 00 00                  call 0x1408d78a4
008D73F5  48 8B D7                        mov rdx, rdi
008D73F8  48 8B CE                        mov rcx, rsi
008D73FB  E8 30 00 00 00                  call 0x1408d7430
008D7400  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
008D7405  8B C3                           mov eax, ebx
008D7407  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008D740C  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
008D7411  48 83 C4 20                     add rsp, 0x20
008D7415  5F                              pop rdi
008D7416  C3                              ret
008D7417  CC                              int3
008D7418  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008D741D  EB E1                           jmp 0x1408d7400
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCovSampCaptureUserAddresses(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = EtwpCovSampCaptureBufferGet(a1, a2, a3, a4);
    v_rbx = 0;
    if (result == 0) goto loc_008D7418;
    result = EtwpCovSampCaptureBufferAddIP(result, a2, a3, a4);
    result = EtwpCovSampCaptureUserStack(result, a2, a3, a4);
    result = EtwpCovSampCaptureBufferMapAddressesAndQueue(a1, result, a3, a4);
loc_008D7400:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_008D7418:
    goto loc_008D7400;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCovSampCaptureUserAddresses(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = EtwpCovSampCaptureBufferGet(Arg1, Arg2, a3, a4);
    local_rbx = 0;
    if (result == 0) goto loc_008D7418;
    result = EtwpCovSampCaptureBufferAddIP(result, Arg2, a3, a4);
    result = EtwpCovSampCaptureUserStack(result, Arg2, a3, a4);
    result = EtwpCovSampCaptureBufferMapAddressesAndQueue(Arg1, result, a3, a4);
loc_008D7400:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_008D7418:
    goto loc_008D7400;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D73BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008D73BC[BB_008D73BC]
  bb_008D73E5[BB_008D73E5]
  bb_008D7400[BB_008D7400]
  bb_008D7417[BB_008D7417]
  bb_008D7418[BB_008D7418]
  bb_008D73BC -->|branch| bb_008D7418
  bb_008D73BC -->|fallthrough| bb_008D73E5
  bb_008D73E5 -->|flow| bb_008D7400
  bb_008D7417 -->|flow| bb_008D7418
  bb_008D7418 -->|branch| bb_008D7400
```
