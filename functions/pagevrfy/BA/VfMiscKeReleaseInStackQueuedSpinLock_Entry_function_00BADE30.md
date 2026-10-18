# VfMiscKeReleaseInStackQueuedSpinLock_Entry

- RVA: `0x00BADE30`–`0x00BADE9B` (길이 `107` bytes)
- VA: `0x0000000140BADE30`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000718AC`
- 디코드: `29`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BADE73` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)
- `0x00BADE85` → [ViMiscCheckKeLowerIrql](../BB/ViMiscCheckKeLowerIrql_function_00BB81C4.md) (function, `0x00BB81C4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BADE30  4C 8B DC                        mov r11, rsp
00BADE33  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00BADE37  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00BADE3B  57                              push rdi
00BADE3C  48 83 EC 40                     sub rsp, 0x40
00BADE40  48 8B F9                        mov rdi, rcx
00BADE43  44 0F 20 C6                     mov rsi, cr8
00BADE47  40 80 FE 02                     cmp sil, 2
00BADE4B  73 2B                           jae 0x140bade78
00BADE4D  48 8B 01                        mov rax, qword ptr [rcx]
00BADE50  BA 32 00 00 00                  mov edx, 0x32
00BADE55  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
00BADE59  B9 C4 00 00 00                  mov ecx, 0xc4
00BADE5E  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00BADE62  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BADE6A  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
00BADE6F  44 0F B6 C6                     movzx r8d, sil
00BADE73  E8 8C FA FE FF                  call 0x140b9d904
00BADE78  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00BADE7C  40 8A CE                        mov cl, sil
00BADE7F  4C 8B 07                        mov r8, qword ptr [rdi]
00BADE82  8A 52 10                        mov dl, byte ptr [rdx + 0x10]
00BADE85  E8 3A A3 00 00                  call 0x140bb81c4
00BADE8A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00BADE8F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00BADE94  48 83 C4 40                     add rsp, 0x40
00BADE98  5F                              pop rdi
00BADE99  C3                              ret
00BADE9A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscKeReleaseInStackQueuedSpinLock_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (64);
    if (((unsigned __int8)(v_cr8)) < 2) {
        result = *(unsigned __int64 *)(a1);
        a2 = 50;
        a4 = *(unsigned __int64 *)(a1 + 8);
        a1 = 196;
        *(unsigned __int64 *)(v_rsp - 24) = result;
        v_stack_m20 = 11;
        a3 = (unsigned __int8)(v_cr8);
        result = CarReportRuleViolationFromNt(a1, a2, a3, a4);
    }
    result = ViMiscCheckKeLowerIrql((unsigned __int8)(v_cr8), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16), *(unsigned __int64 *)(a1), a4);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscKeReleaseInStackQueuedSpinLock_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (64);
    if (((uint8_t)(v_cr8)) < 2) {
        result = *(uint64_t *)(arg1);
        a2 = 50;
        a4 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = 196;
        *(uint64_t *)(local_rsp - 0x18) = result;
        v_stack_m20 = 11;
        a3 = (uint8_t)(v_cr8);
        result = CarReportRuleViolationFromNt(Arg1, a2, a3, a4);
    }
    result = ViMiscCheckKeLowerIrql((uint8_t)(v_cr8), *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10), *(uint64_t *)(arg1), a4);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BADE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BADE30[BB_00BADE30]
  bb_00BADE4D[BB_00BADE4D]
  bb_00BADE78[BB_00BADE78]
  bb_00BADE9A[BB_00BADE9A]
  bb_00BADE30 -->|branch| bb_00BADE78
  bb_00BADE30 -->|fallthrough| bb_00BADE4D
  bb_00BADE4D -->|flow| bb_00BADE78
```
