# VfThunkRemoveTargetNotify

- RVA: `0x00BA72AC`–`0x00BA72DD` (길이 `49` bytes)
- VA: `0x0000000140BA72AC`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA72BF` → [ViThunkFreeSharedThunksArray](../BB/ViThunkFreeSharedThunksArray_function_00BB6590.md) (function, `0x00BB6590`)
- `0x00BA72C8` → [ViThunkFreeSharedThunksArray](../BB/ViThunkFreeSharedThunksArray_function_00BB6590.md) (function, `0x00BB6590`)
- `0x00BA72D1` → [ViThunkFreeSharedThunksArray](../BB/ViThunkFreeSharedThunksArray_function_00BB6590.md) (function, `0x00BB6590`)

### Direct callers
- [VfTargetDriversRemove](../../text/3E/VfTargetDriversRemove_function_003EEF9C.md) at `0x003EF191`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA72AC  40 53                           push rbx
00BA72AE  48 83 EC 20                     sub rsp, 0x20
00BA72B2  48 8B D9                        mov rbx, rcx
00BA72B5  48 83 C1 10                     add rcx, 0x10
00BA72B9  8B 01                           mov eax, dword ptr [rcx]
00BA72BB  A8 01                           test al, 1
00BA72BD  75 17                           jne 0x140ba72d6
00BA72BF  E8 CC F2 00 00                  call 0x140bb6590
00BA72C4  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00BA72C8  E8 C3 F2 00 00                  call 0x140bb6590
00BA72CD  48 8D 4B 20                     lea rcx, [rbx + 0x20]
00BA72D1  E8 BA F2 00 00                  call 0x140bb6590
00BA72D6  48 83 C4 20                     add rsp, 0x20
00BA72DA  5B                              pop rbx
00BA72DB  C3                              ret
00BA72DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfThunkRemoveTargetNotify(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (16);
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) == 0) {
        result = ViThunkFreeSharedThunksArray(a1, a2, a3, a4);
        a1 = a1 + 24;
        result = ViThunkFreeSharedThunksArray(a1, a2, a3, a4);
        a1 = a1 + 32;
        result = ViThunkFreeSharedThunksArray(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfThunkRemoveTargetNotify(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (16);
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) == 0) {
        result = ViThunkFreeSharedThunksArray(Arg1, a2, a3, a4);
        Arg1 = Arg1 + 24;
        result = ViThunkFreeSharedThunksArray(Arg1, a2, a3, a4);
        Arg1 = Arg1 + 32;
        result = ViThunkFreeSharedThunksArray(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA72AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA72AC[BB_00BA72AC]
  bb_00BA72BF[BB_00BA72BF]
  bb_00BA72D6[BB_00BA72D6]
  bb_00BA72DC[BB_00BA72DC]
  bb_00BA72AC -->|branch| bb_00BA72D6
  bb_00BA72AC -->|fallthrough| bb_00BA72BF
  bb_00BA72BF -->|flow| bb_00BA72D6
```
