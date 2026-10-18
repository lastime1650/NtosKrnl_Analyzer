# PfpPrefetchSharedDeref

- RVA: `0x00939E78`–`0x00939EA7` (길이 `47` bytes)
- VA: `0x0000000140939E78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00939E93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PfpQueryFileExtentsRequest](../75/PfpQueryFileExtentsRequest_function_007508E8.md) at `0x00750F3A`
- [PfpPrefetchRequestPerform](PfpPrefetchRequestPerform_function_00938F74.md) at `0x009393EC`
- [PfSnCleanupPrefetchHeader](PfSnCleanupPrefetchHeader_function_00939898.md) at `0x0093995D`
- [PfpPrefetchSharedConflictNotifyEnd](../AC/PfpPrefetchSharedConflictNotifyEnd_function_00AC1210.md) at `0x00AC1259`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00939E93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00939E78  48 83 EC 28                     sub rsp, 0x28
00939E7C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00939E80  F0 48 0F C1 41 78               lock xadd qword ptr [rcx + 0x78], rax
00939E86  48 83 E8 01                     sub rax, 1
00939E8A  7F 0C                           jg 0x140939e98
00939E8C  48 85 C0                        test rax, rax
00939E8F  75 0D                           jne 0x140939e9e
00939E91  33 D2                           xor edx, edx
00939E93  E8 D8 89 24 00                  call 0x140b82870
00939E98  48 83 C4 28                     add rsp, 0x28
00939E9C  C3                              ret
00939E9D  CC                              int3
00939E9E  B9 0E 00 00 00                  mov ecx, 0xe
00939EA3  CD 29                           int 0x29
00939EA5  EB F1                           jmp 0x140939e98
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpPrefetchSharedDeref(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_00939E98;
    if (result != 0) goto loc_00939E9E;
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
loc_00939E98:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00939E9E:
    goto loc_00939E98;
}
```

## 5. (Beta) C Style

```c
int64_t PfpPrefetchSharedDeref(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_00939E98;
    if (result != 0) goto loc_00939E9E;
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
loc_00939E98:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00939E9E:
    goto loc_00939E98;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00939E78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00939E78[BB_00939E78]
  bb_00939E8C[BB_00939E8C]
  bb_00939E91[BB_00939E91]
  bb_00939E98[BB_00939E98]
  bb_00939E9D[BB_00939E9D]
  bb_00939E9E[BB_00939E9E]
  bb_00939E78 -->|branch| bb_00939E98
  bb_00939E78 -->|fallthrough| bb_00939E8C
  bb_00939E8C -->|branch| bb_00939E9E
  bb_00939E8C -->|fallthrough| bb_00939E91
  bb_00939E91 -->|flow| bb_00939E98
  bb_00939E9D -->|flow| bb_00939E9E
  bb_00939E9E -->|branch| bb_00939E98
```
