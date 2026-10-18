# PopFxNextComponentChildRelationSafe

- RVA: `0x00450C70`–`0x00450C96` (길이 `38` bytes)
- VA: `0x0000000140450C70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7338`
- 디코드: `11`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PoFxRemoveComponentRelation](../5D/PoFxRemoveComponentRelation_function_005D1C90.md) at `0x005D1E67`
- [PoFxRemoveDeviceRelation](../5D/PoFxRemoveDeviceRelation_function_005D1EF0.md) at `0x005D2090`
- [PopFxComponentRelationsCleanup](../5D/PopFxComponentRelationsCleanup_function_005D221C.md) at `0x005D22FE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00450C8D` → [sub_00450D22](Unknown_function_00450D22.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00450C70  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00450C75  56                              push rsi
00450C76  57                              push rdi
00450C77  41 56                           push r14
00450C79  48 83 EC 20                     sub rsp, 0x20
00450C7D  48 8D 99 B8 01 00 00            lea rbx, [rcx + 0x1b8]
00450C84  49 8B F0                        mov rsi, r8
00450C87  48 8B FA                        mov rdi, rdx
00450C8A  48 85 D2                        test rdx, rdx
00450C8D  0F 85 8F 00 00 00               jne 0x140450d22
00450C93  48 8B FB                        mov rdi, rbx
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PopFxNextComponentChildRelationSafe(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (32);
    return;
}
```

## 5. (Beta) C Style

```c
void PopFxNextComponentChildRelationSafe(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (32);
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1B8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00450C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00450C70[BB_00450C70]
  bb_00450C93[BB_00450C93]
  bb_00450C70 -->|fallthrough| bb_00450C93
```
