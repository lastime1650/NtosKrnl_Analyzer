# ViThunkFreeSharedThunksArray

- RVA: `0x00BB6590`–`0x00BB65B6` (길이 `38` bytes)
- VA: `0x0000000140BB6590`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BB65A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [VfThunkRemoveTargetNotify](../BA/VfThunkRemoveTargetNotify_function_00BA72AC.md) at `0x00BA72BF`
- [VfThunkRemoveTargetNotify](../BA/VfThunkRemoveTargetNotify_function_00BA72AC.md) at `0x00BA72C8`
- [VfThunkRemoveTargetNotify](../BA/VfThunkRemoveTargetNotify_function_00BA72AC.md) at `0x00BA72D1`
- [ViThunkCreateSharedExportInformation](ViThunkCreateSharedExportInformation_function_00BB637C.md) at `0x00BB63F5`
- [VfThunkAddTargetNotify](VfThunkAddTargetNotify_function_00BB64E4.md) at `0x00BB6517`
- [VfThunkAddTargetNotify](VfThunkAddTargetNotify_function_00BB64E4.md) at `0x00BB6520`
- [VfThunkAddTargetNotify](VfThunkAddTargetNotify_function_00BB64E4.md) at `0x00BB6529`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB65A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGEVRFY` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB6590  40 53                           push rbx
00BB6592  48 83 EC 20                     sub rsp, 0x20
00BB6596  48 8B D9                        mov rbx, rcx
00BB6599  48 8B 09                        mov rcx, qword ptr [rcx]
00BB659C  48 85 C9                        test rcx, rcx
00BB659F  74 0E                           je 0x140bb65af
00BB65A1  BA 56 66 49 54                  mov edx, 0x54496656
00BB65A6  E8 C5 C2 FC FF                  call 0x140b82870
00BB65AB  48 83 23 00                     and qword ptr [rbx], 0
00BB65AF  48 83 C4 20                     add rsp, 0x20
00BB65B3  5B                              pop rbx
00BB65B4  C3                              ret
00BB65B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViThunkFreeSharedThunksArray(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1) != 0) {
        a2 = 0x54496656ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViThunkFreeSharedThunksArray(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1) != 0) {
        a2 = 0x54496656ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB6590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB6590[BB_00BB6590]
  bb_00BB65A1[BB_00BB65A1]
  bb_00BB65AF[BB_00BB65AF]
  bb_00BB65B5[BB_00BB65B5]
  bb_00BB6590 -->|branch| bb_00BB65AF
  bb_00BB6590 -->|fallthrough| bb_00BB65A1
  bb_00BB65A1 -->|flow| bb_00BB65AF
```
