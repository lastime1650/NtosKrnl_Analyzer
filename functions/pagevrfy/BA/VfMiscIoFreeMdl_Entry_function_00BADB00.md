# VfMiscIoFreeMdl_Entry

- RVA: `0x00BADB00`–`0x00BADB57` (길이 `87` bytes)
- VA: `0x0000000140BADB00`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `25`개 명령, `87/87` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BADB14` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (function, `0x004BC694`)
- `0x00BADB4B` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BADB14` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BADB00  40 53                           push rbx
00BADB02  48 83 EC 40                     sub rsp, 0x40
00BADB06  48 8B D9                        mov rbx, rcx
00BADB09  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00BADB0D  0F B7 51 08                     movzx edx, word ptr [rcx + 8]
00BADB11  4C 8B 03                        mov r8, qword ptr [rbx]
00BADB14  E8 7B EB 90 FF                  call 0x1404bc694
00BADB19  4C 8B 43 08                     mov r8, qword ptr [rbx + 8]
00BADB1D  49 0F BF 48 0A                  movsx rcx, word ptr [r8 + 0xa]
00BADB22  8A C1                           mov al, cl
00BADB24  24 11                           and al, 0x11
00BADB26  3C 01                           cmp al, 1
00BADB28  75 26                           jne 0x140badb50
00BADB2A  48 8B 03                        mov rax, qword ptr [rbx]
00BADB2D  BA B8 00 00 00                  mov edx, 0xb8
00BADB32  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BADB37  4C 8B C9                        mov r9, rcx
00BADB3A  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BADB42  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BADB48  8D 4A 0C                        lea ecx, [rdx + 0xc]
00BADB4B  E8 B4 FD FE FF                  call 0x140b9d904
00BADB50  48 83 C4 40                     add rsp, 0x40
00BADB54  5B                              pop rbx
00BADB55  C3                              ret
00BADB56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscIoFreeMdl_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    result = VfMiscCheckKernelAddress(*(unsigned __int64 *)(a1 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 8), *(unsigned __int64 *)(a1), a4);
    result = (unsigned __int8)(((unsigned __int8)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 10)))) & (17));
    if (((unsigned __int8)(result)) == 1) {
        result = *(unsigned __int64 *)(a1);
        a2 = 184;
        v_stack_m18 = result;
        a4 = (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 10));
        v_stack_m20 = 11;
        a1 = a2 + 12;
        result = CarReportRuleViolationFromNt(a1, a2, *(unsigned __int64 *)(a1 + 8), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscIoFreeMdl_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    result = VfMiscCheckKernelAddress(*(uint64_t *)(arg1 + 0x8), *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8), *(uint64_t *)(arg1), a4);
    result = (uint8_t)(((uint8_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xA)))) & (17));
    if (((uint8_t)(result)) == 1) {
        result = *(uint64_t *)(arg1);
        a2 = 184;
        v_stack_m18 = result;
        a4 = (int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xA));
        v_stack_m20 = 11;
        Arg1 = a2 + 12;
        result = CarReportRuleViolationFromNt(Arg1, a2, *(uint64_t *)(arg1 + 0x8), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BADB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BADB00[BB_00BADB00]
  bb_00BADB2A[BB_00BADB2A]
  bb_00BADB50[BB_00BADB50]
  bb_00BADB56[BB_00BADB56]
  bb_00BADB00 -->|branch| bb_00BADB50
  bb_00BADB00 -->|fallthrough| bb_00BADB2A
  bb_00BADB2A -->|flow| bb_00BADB50
```
