# KiNotifyAvailableCpusChangeProcess

- RVA: `0x004FCE30`–`0x004FCE53` (길이 `35` bytes)
- VA: `0x00000001404FCE30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FCE48` → [KiAvailableCpusSubscriptionQueueWorkItem](KiAvailableCpusSubscriptionQueueWorkItem_function_004FCE5C.md) (function, `0x004FCE5C`)

### Direct callers
- [KeSetAffinityProcess](../3C/KeSetAffinityProcess_function_003C0A60.md) at `0x003C0C86`
- [KiAvailableCpusPartitionWorkItemCallback](../5B/KiAvailableCpusPartitionWorkItemCallback_function_005B9990.md) at `0x005B9A62`
- [KeAssignCpuPartitionsToProcess](../5C/KeAssignCpuPartitionsToProcess_function_005C08D0.md) at `0x005C0A84`
- [KeCpuPartitionMoveCpus](../5C/KeCpuPartitionMoveCpus_function_005C0B70.md) at `0x005C0D07`
- [KeCpuPartitionMoveCpus](../5C/KeCpuPartitionMoveCpus_function_005C0B70.md) at `0x005C0D54`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FCE30  48 83 EC 28                     sub rsp, 0x28
004FCE34  48 8B 89 C0 01 00 00            mov rcx, qword ptr [rcx + 0x1c0]
004FCE3B  48 8D 41 28                     lea rax, [rcx + 0x28]
004FCE3F  48 39 00                        cmp qword ptr [rax], rax
004FCE42  74 09                           je 0x1404fce4d
004FCE44  48 83 C1 38                     add rcx, 0x38
004FCE48  E8 0F 00 00 00                  call 0x1404fce5c
004FCE4D  48 83 C4 28                     add rsp, 0x28
004FCE51  C3                              ret
004FCE52  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiNotifyAvailableCpusChangeProcess(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(a1 + 448) + 40;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 448) + 40)) != (*(unsigned __int64 *)(a1 + 448) + 40)) {
        a1 = (*(unsigned __int64 *)(a1 + 448)) + (56);
        result = KiAvailableCpusSubscriptionQueueWorkItem(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiNotifyAvailableCpusChangeProcess(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(arg1 + 0x1C0) + 40;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1C0) + 0x28)) != (*(uint64_t *)(arg1 + 0x1C0) + 40)) {
        Arg1 = (*(uint64_t *)(arg1 + 0x1C0)) + (56);
        result = KiAvailableCpusSubscriptionQueueWorkItem(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1C0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FCE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FCE30[BB_004FCE30]
  bb_004FCE44[BB_004FCE44]
  bb_004FCE4D[BB_004FCE4D]
  bb_004FCE52[BB_004FCE52]
  bb_004FCE30 -->|branch| bb_004FCE4D
  bb_004FCE30 -->|fallthrough| bb_004FCE44
  bb_004FCE44 -->|flow| bb_004FCE4D
```
