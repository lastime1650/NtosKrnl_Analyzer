# IopSymlinkGetECP

- RVA: `0x00458288`–`0x004582A4` (길이 `28` bytes)
- VA: `0x0000000140458288`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00458299` → [FsRtlFindExtraCreateParameter](../../page/97/FsRtlFindExtraCreateParameter_function_0097AFE0.md) (function, `0x0097AFE0`)

### Direct callers
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089F904`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089FEA0`
- [IopSymlinkUpdateECP](../../page/8A/IopSymlinkUpdateECP_function_008A20CC.md) at `0x008A2110`
- [IopSymlinkProcessReparse](../../page/A3/IopSymlinkProcessReparse_function_00A330B4.md) at `0x00A33117`
- [IopGraftName](../../page/A3/IopGraftName_function_00A33160.md) at `0x00A331D6`
- [sub_00B39F44](../../page/B3/Unknown_function_00B39F44.md) at `0x00B39FD4`

### Static image references
- `0x00458292` → RVA `0x00B4B100` (`IopSymlinkECPGuid`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00458299` → [FsRtlFindExtraCreateParameter](../../page/97/FsRtlFindExtraCreateParameter_function_0097AFE0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00458288  48 83 EC 28                     sub rsp, 0x28
0045828C  4C 8B C2                        mov r8, rdx
0045828F  45 33 C9                        xor r9d, r9d
00458292  48 8D 15 67 2E 6F 00            lea rdx, [rip + 0x6f2e67]
00458299  E8 42 2D 52 00                  call 0x14097afe0
0045829E  48 83 C4 28                     add rsp, 0x28
004582A2  C3                              ret
004582A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopSymlinkGetECP(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    result = FsRtlFindExtraCreateParameter(a1, v_rip + 7286375, a2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopSymlinkGetECP(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    result = FsRtlFindExtraCreateParameter(Arg1, v_rip + 7286375, Arg2, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00458288&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00458288[BB_00458288]
  bb_004582A3[BB_004582A3]
```
