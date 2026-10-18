# CmpGetSecurityCacheEntryForKcbStack

- RVA: `0x008C7580`–`0x008C7598` (길이 `24` bytes)
- VA: `0x00000001408C7580`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083E50`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpCheckKcbStackAccess](../70/CmpCheckKcbStackAccess_function_00701174.md) at `0x00701187`
- [CmSetValueKey](../84/CmSetValueKey_function_008457C0.md) at `0x008465D7`
- [CmDeleteValueKey](../84/CmDeleteValueKey_function_008476E8.md) at `0x0084822F`
- [CmpCheckCreateAccessOnKcbStack](CmpCheckCreateAccessOnKcbStack_function_008C7010.md) at `0x008C7040`
- [CmpCheckKeyOwnerForPca](CmpCheckKeyOwnerForPca_function_008C7130.md) at `0x008C7144`
- [CmpNotifyTriggerCheck](CmpNotifyTriggerCheck_function_008C74A4.md) at `0x008C74FD`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948936`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948A14`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C7580  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008C7585  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
008C758A  56                              push rsi
008C758B  57                              push rdi
008C758C  41 57                           push r15
008C758E  48 83 EC 20                     sub rsp, 0x20
008C7592  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
008C7596  33 FF                           xor edi, edi
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetSecurityCacheEntryForKcbStack(__int64 a1)
{
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rbp;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    return *(unsigned __int16 *)(a1 + 2);
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetSecurityCacheEntryForKcbStack(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rbp;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    return *(uint16_t *)(arg1 + 0x2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C7580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C7580[BB_008C7580]
```
