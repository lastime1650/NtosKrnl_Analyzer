# MmFreePagesFromMdl

- RVA: `0x003F82E0`–`0x003F82F7` (길이 `23` bytes)
- VA: `0x00000001403F82E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003F82EC` → [MiFreePagesFromMdl](MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)

### Direct callers
- [sub_0051ADC0](../51/Unknown_function_0051ADC0.md) at `0x0051ADF5`
- [PopFreeHiberContext](../../page/70/PopFreeHiberContext_function_00704F1C.md) at `0x00704FAF`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x00709062`
- [HalpDmaAllocateLocalScatterPool](../../page/70/HalpDmaAllocateLocalScatterPool_function_007091D4.md) at `0x007092BB`
- [IoReserveKsrPersistentMemoryEx](../../page/72/IoReserveKsrPersistentMemoryEx_function_007248C0.md) at `0x00724BF4`
- [EtwpFreePfnArray](../../page/7B/EtwpFreePfnArray_function_007B66A8.md) at `0x007B66FC`
- [EtwpFreePfnArray](../../page/7B/EtwpFreePfnArray_function_007B66A8.md) at `0x007B6721`
- [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) at `0x007FBC1C`
- [HalpDmaAllocateScatterMemory](../../page/AA/HalpDmaAllocateScatterMemory_function_00AA2D70.md) at `0x00AA2DEC`
- [MmFreeNonCachedMemory](../../page/AB/MmFreeNonCachedMemory_function_00AB4640.md) at `0x00AB46B3`
- [HalpDmaGrowContiguousMapBuffers](../../page/AD/HalpDmaGrowContiguousMapBuffers_function_00AD6D14.md) at `0x00AD6DF2`
- [sub_00B49968](../../page/B4/Unknown_function_00B49968.md) at `0x00B4996B`
- [ResFwFreeContext](../../pagebgfx/BC/ResFwFreeContext_function_00BC34C4.md) at `0x00BC34E6`
- [ResFwFreeContext](../../pagebgfx/BC/ResFwFreeContext_function_00BC34C4.md) at `0x00BC352A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F82E0  48 83 EC 28                     sub rsp, 0x28
003F82E4  45 33 C9                        xor r9d, r9d
003F82E7  45 33 C0                        xor r8d, r8d
003F82EA  33 D2                           xor edx, edx
003F82EC  E8 0F 00 00 00                  call 0x1403f8300
003F82F1  48 83 C4 28                     add rsp, 0x28
003F82F5  C3                              ret
003F82F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmFreePagesFromMdl(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = MiFreePagesFromMdl(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmFreePagesFromMdl(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = MiFreePagesFromMdl(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F82E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F82E0[BB_003F82E0]
  bb_003F82F6[BB_003F82F6]
```
