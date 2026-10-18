# CmpLogTransactionAbortedForRollbackPacket

- RVA: `0x009AE7F4`–`0x009AE80F` (길이 `27` bytes)
- VA: `0x00000001409AE7F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009AE804` → [CmpLogTransactionAbortedWithChildName](CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)

### Direct callers
- [CmpTryToRundownHive](../../text/2A/CmpTryToRundownHive_function_002A4A60.md) at `0x002A4B6A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009AE7F4  48 83 EC 38                     sub rsp, 0x38
009AE7F8  41 8B 00                        mov eax, dword ptr [r8]
009AE7FB  44 8B C2                        mov r8d, edx
009AE7FE  33 D2                           xor edx, edx
009AE800  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009AE804  E8 67 05 00 00                  call 0x1409aed70
009AE809  48 83 C4 38                     add rsp, 0x38
009AE80D  C3                              ret
009AE80E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLogTransactionAbortedForRollbackPacket(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a2 = 0;
    v_stack_m18 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    result = CmpLogTransactionAbortedWithChildName(a1, a2, (unsigned int)(a2), a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLogTransactionAbortedForRollbackPacket(int64_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg2 = 0;
    v_stack_m18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    result = CmpLogTransactionAbortedWithChildName(Arg1, Arg2, (uint32_t)(Arg2), a4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009AE7F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009AE7F4[BB_009AE7F4]
  bb_009AE80E[BB_009AE80E]
```
