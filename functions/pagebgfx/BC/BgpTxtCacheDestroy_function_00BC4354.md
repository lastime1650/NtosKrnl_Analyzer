# BgpTxtCacheDestroy

- RVA: `0x00BC4354`–`0x00BC4373` (길이 `31` bytes)
- VA: `0x0000000140BC4354`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BC4358` → [TxtpClearCache](TxtpClearCache_function_00BC437C.md) (function, `0x00BC437C`)
- `0x00BC436C` → [RaspClearCache](RaspClearCache_function_00BC5C90.md) (function, `0x00BC5C90`)

### Direct callers
- [AnFwDisplayProgressIndicator](AnFwDisplayProgressIndicator_function_00BC1FD0.md) at `0x00BC219B`
- [BgpTxtDestroyRegion](BgpTxtDestroyRegion_function_00BC2B5C.md) at `0x00BC2B93`
- [ResFwFreeContext](ResFwFreeContext_function_00BC34C4.md) at `0x00BC34FB`
- [AnFwpDisableProgressTimer](AnFwpDisableProgressTimer_function_00BC3CB4.md) at `0x00BC3CE1`

### Static image references
- `0x00BC435D` → RVA `0x00EF02E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC4354  48 83 EC 28                     sub rsp, 0x28
00BC4358  E8 1F 00 00 00                  call 0x140bc437c
00BC435D  80 3D 84 BF 32 00 00            cmp byte ptr [rip + 0x32bf84], 0
00BC4364  75 06                           jne 0x140bc436c
00BC4366  48 83 C4 28                     add rsp, 0x28
00BC436A  C3                              ret
00BC436B  CC                              int3
00BC436C  E8 1F 19 00 00                  call 0x140bc5c90
00BC4371  EB F3                           jmp 0x140bc4366
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpTxtCacheDestroy(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = TxtpClearCache(a1, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 3325828)) != 0) goto loc_00BC436C;
loc_00BC4366:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00BC436C:
    result = RaspClearCache(a1, a2, a3, a4);
    goto loc_00BC4366;
}
```

## 5. (Beta) C Style

```c
void BgpTxtCacheDestroy(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = TxtpClearCache(a1, a2, a3, a4);
    if ((*(uint8_t *)(v_rip + 0x32BF84)) != 0) goto loc_00BC436C;
loc_00BC4366:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00BC436C:
    result = RaspClearCache(a1, a2, a3, a4);
    goto loc_00BC4366;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC4354&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC4354[BB_00BC4354]
  bb_00BC4366[BB_00BC4366]
  bb_00BC436B[BB_00BC436B]
  bb_00BC436C[BB_00BC436C]
  bb_00BC4354 -->|branch| bb_00BC436C
  bb_00BC4354 -->|fallthrough| bb_00BC4366
  bb_00BC436B -->|flow| bb_00BC436C
  bb_00BC436C -->|branch| bb_00BC4366
```
