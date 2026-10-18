# MmGetFileObjectForSection

- RVA: `0x008D68E0`–`0x008D68FF` (길이 `31` bytes)
- VA: `0x00000001408D68E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008D68E4` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x008D68F4` → [MiReferenceControlAreaFileWithTag](../../text/34/MiReferenceControlAreaFileWithTag_function_00348390.md) (function, `0x00348390`)

### Direct callers
- [FsRtlCreateSectionForDataScan](../../text/45/FsRtlCreateSectionForDataScan_function_00453330.md) at `0x00453461`
- [DbgkCreateThread](DbgkCreateThread_function_008D5E34.md) at `0x008D609C`
- [PsReferenceProcessFilePointer](PsReferenceProcessFilePointer_function_008D6870.md) at `0x008D68A4`
- [PspInitializeFullProcessImageName](../A4/PspInitializeFullProcessImageName_function_00A4345C.md) at `0x00A43620`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008D68E4` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x008D68F4` → [MiReferenceControlAreaFileWithTag](../../text/34/MiReferenceControlAreaFileWithTag_function_00348390.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D68E0  48 83 EC 28                     sub rsp, 0x28
008D68E4  E8 C7 E3 9B FF                  call 0x140294cb0
008D68E9  BA 44 66 6C 74                  mov edx, 0x746c6644
008D68EE  48 8B C8                        mov rcx, rax
008D68F1  45 33 C0                        xor r8d, r8d
008D68F4  E8 97 1A A7 FF                  call 0x140348390
008D68F9  48 83 C4 28                     add rsp, 0x28
008D68FD  C3                              ret
008D68FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmGetFileObjectForSection(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiSectionControlArea(a1, a2, a3, a4);
    a3 = 0;
    result = MiReferenceControlAreaFileWithTag(result, (unsigned int)(0x746C6644ULL), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmGetFileObjectForSection(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiSectionControlArea(Arg1, Arg2, Arg3, a4);
    Arg3 = 0;
    result = MiReferenceControlAreaFileWithTag(result, (uint32_t)(0x746C6644ULL), Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D68E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008D68E0[BB_008D68E0]
  bb_008D68FE[BB_008D68FE]
```
