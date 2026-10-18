# IopSymlinkRemoveECP

- RVA: `0x00446480`–`0x0044649C` (길이 `28` bytes)
- VA: `0x0000000140446480`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00446491` → [FsRtlRemoveExtraCreateParameter](../../page/9A/FsRtlRemoveExtraCreateParameter_function_009A8580.md) (function, `0x009A8580`)

### Direct callers
- [IopSymlinkPropagateToExtensionIfNeeded](../../page/8A/IopSymlinkPropagateToExtensionIfNeeded_function_008A1580.md) at `0x008A15B9`
- [IopSymlinkUpdateECP](../../page/8A/IopSymlinkUpdateECP_function_008A20CC.md) at `0x008A218A`
- [sub_00B39C68](../../page/B3/Unknown_function_00B39C68.md) at `0x00B39E5D`

### Static image references
- `0x0044648A` → RVA `0x00B4B100` (`IopSymlinkECPGuid`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00446491` → [FsRtlRemoveExtraCreateParameter](../../page/9A/FsRtlRemoveExtraCreateParameter_function_009A8580.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00446480  48 83 EC 28                     sub rsp, 0x28
00446484  4C 8B C2                        mov r8, rdx
00446487  45 33 C9                        xor r9d, r9d
0044648A  48 8D 15 6F 4C 70 00            lea rdx, [rip + 0x704c6f]
00446491  E8 EA 20 56 00                  call 0x1409a8580
00446496  48 83 C4 28                     add rsp, 0x28
0044649A  C3                              ret
0044649B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopSymlinkRemoveECP(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    result = FsRtlRemoveExtraCreateParameter(a1, v_rip + 7359599, a2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopSymlinkRemoveECP(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    result = FsRtlRemoveExtraCreateParameter(Arg1, v_rip + 7359599, Arg2, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00446480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00446480[BB_00446480]
  bb_0044649B[BB_0044649B]
```
