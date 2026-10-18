# HvMarkDirtyForFlush

- RVA: `0x00494CA4`–`0x00494CB9` (길이 `21` bytes)
- VA: `0x0000000140494CA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00494CAE` → [HvpMarkDirty](../../page/85/HvpMarkDirty_function_008593C0.md) (function, `0x008593C0`)

### Direct callers
- [CmpFlushHive](../../page/9B/CmpFlushHive_function_009B3DC0.md) at `0x009B448C`
- [HvFoldBackDirtyData](../../page/A4/HvFoldBackDirtyData_function_00A463B8.md) at `0x00A46429`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00494CAE` → [HvpMarkDirty](../../page/85/HvpMarkDirty_function_008593C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00494CA4  48 83 EC 28                     sub rsp, 0x28
00494CA8  41 B9 02 00 00 00               mov r9d, 2
00494CAE  E8 0D 47 3C 00                  call 0x1408593c0
00494CB3  48 83 C4 28                     add rsp, 0x28
00494CB7  C3                              ret
00494CB8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvMarkDirtyForFlush(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HvpMarkDirty(a1, a2, a3, 2);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HvMarkDirtyForFlush(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HvpMarkDirty(a1, a2, a3, 2);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00494CA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00494CA4[BB_00494CA4]
  bb_00494CB8[BB_00494CB8]
```
