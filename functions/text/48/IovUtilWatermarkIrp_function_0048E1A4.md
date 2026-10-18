# IovUtilWatermarkIrp

- RVA: `0x0048E1A4`–`0x0048E1BE` (길이 `26` bytes)
- VA: `0x000000014048E1A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0048E1B7` → [VfIrpWatermark](../../pagevrfy/B9/VfIrpWatermark_function_00B9E070.md) (function, `0x00B9E070`)

### Direct callers
- [IopEjectDevice](../../page/73/IopEjectDevice_function_0073DC84.md) at `0x0073DD93`
- [IopSynchronousCall](../../page/8F/IopSynchronousCall_function_008FB018.md) at `0x008FB083`
- [PnpAsynchronousCall](../../page/A6/PnpAsynchronousCall_function_00A635D0.md) at `0x00A6361F`
- [IopFilterResourceRequirementsCall](../../page/A9/IopFilterResourceRequirementsCall_function_00A92388.md) at `0x00A923FF`
- [VfIrpSendSynchronousIrp](../../pagevrfy/B9/VfIrpSendSynchronousIrp_function_00B9DEF0.md) at `0x00B9DF75`

### Static image references
- `0x0048E1A8` → RVA `0x00F048E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0048E1B7` → [VfIrpWatermark](../../pagevrfy/B9/VfIrpWatermark_function_00B9E070.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048E1A4  48 83 EC 28                     sub rsp, 0x28
0048E1A8  83 3D 31 67 A7 00 00            cmp dword ptr [rip + 0xa76731], 0
0048E1AF  75 06                           jne 0x14048e1b7
0048E1B1  48 83 C4 28                     add rsp, 0x28
0048E1B5  C3                              ret
0048E1B6  CC                              int3
0048E1B7  E8 B4 FE 70 00                  call 0x140b9e070
0048E1BC  EB F3                           jmp 0x14048e1b1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovUtilWatermarkIrp(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 10970929)) != 0) goto loc_0048E1B7;
loc_0048E1B1:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0048E1B7:
    result = VfIrpWatermark(a1, a2, a3, a4);
    goto loc_0048E1B1;
}
```

## 5. (Beta) C Style

```c
void IovUtilWatermarkIrp(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xA76731)) != 0) goto loc_0048E1B7;
loc_0048E1B1:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0048E1B7:
    result = VfIrpWatermark(a1, a2, a3, a4);
    goto loc_0048E1B1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048E1A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048E1A4[BB_0048E1A4]
  bb_0048E1B1[BB_0048E1B1]
  bb_0048E1B6[BB_0048E1B6]
  bb_0048E1B7[BB_0048E1B7]
  bb_0048E1A4 -->|branch| bb_0048E1B7
  bb_0048E1A4 -->|fallthrough| bb_0048E1B1
  bb_0048E1B6 -->|flow| bb_0048E1B7
  bb_0048E1B7 -->|branch| bb_0048E1B1
```
