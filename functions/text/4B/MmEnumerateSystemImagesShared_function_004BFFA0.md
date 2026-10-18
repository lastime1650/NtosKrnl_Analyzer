# MmEnumerateSystemImagesShared

- RVA: `0x004BFFA0`–`0x004BFFB5` (길이 `21` bytes)
- VA: `0x00000001404BFFA0`
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
- `0x004BFFAA` → [MiEnumerateSystemImages](../2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)

### Direct callers
- [ExpQueryModuleInformationEx](../../page/7C/ExpQueryModuleInformationEx_function_007C4A0C.md) at `0x007C4A6E`
- [ExpQueryModuleInformation](../../page/A9/ExpQueryModuleInformation_function_00A9BC30.md) at `0x00A9BC7B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BFFA0  48 83 EC 28                     sub rsp, 0x28
004BFFA4  41 B8 02 00 00 00               mov r8d, 2
004BFFAA  E8 91 3D DE FF                  call 0x1402a3d40
004BFFAF  48 83 C4 28                     add rsp, 0x28
004BFFB3  C3                              ret
004BFFB4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmEnumerateSystemImagesShared(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiEnumerateSystemImages(a1, a2, 2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmEnumerateSystemImagesShared(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiEnumerateSystemImages(a1, a2, 2, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BFFA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BFFA0[BB_004BFFA0]
  bb_004BFFB4[BB_004BFFB4]
```
