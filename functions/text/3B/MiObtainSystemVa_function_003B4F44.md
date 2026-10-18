# MiObtainSystemVa

- RVA: `0x003B4F44`–`0x003B4F66` (길이 `34` bytes)
- VA: `0x00000001403B4F44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003B4F4D` → [MiSystemVaToDynamicBitmap](MiSystemVaToDynamicBitmap_function_003B4F88.md) (function, `0x003B4F88`)
- `0x003B4F5B` → [MiObtainDynamicVa](MiObtainDynamicVa_function_003B501C.md) (function, `0x003B501C`)

### Direct callers
- [MiExpandSystemCache](MiExpandSystemCache_function_003B3DC8.md) at `0x003B3E20`
- [MiGetPageTablesForLargeMap](MiGetPageTablesForLargeMap_function_003B48D4.md) at `0x003B4936`
- [MiReservePoolMemory](MiReservePoolMemory_function_003B4AD8.md) at `0x003B4B26`
- [MiExpandPtes](MiExpandPtes_function_003B4B78.md) at `0x003B4C0C`
- [MiReserveDriverPtes](../../page/A7/MiReserveDriverPtes_function_00A75150.md) at `0x00A75238`
- [MiInitializeSystemPtes](../../init/C6/MiInitializeSystemPtes_function_00C6A998.md) at `0x00C6AB1C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B4F44  48 83 EC 28                     sub rsp, 0x28
003B4F48  44 8B C9                        mov r9d, ecx
003B4F4B  8B CA                           mov ecx, edx
003B4F4D  E8 36 00 00 00                  call 0x1403b4f88
003B4F52  44 8B C2                        mov r8d, edx
003B4F55  48 8B C8                        mov rcx, rax
003B4F58  41 8B D1                        mov edx, r9d
003B4F5B  E8 BC 00 00 00                  call 0x1403b501c
003B4F60  48 83 C4 28                     add rsp, 0x28
003B4F64  C3                              ret
003B4F65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiObtainSystemVa(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiSystemVaToDynamicBitmap((unsigned int)(a2), a2, a3, (unsigned int)(a1));
    result = MiObtainDynamicVa(result, (unsigned int)((unsigned int)((unsigned int)(a1))), (unsigned int)(a2), (unsigned int)(a1));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiObtainSystemVa(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiSystemVaToDynamicBitmap((uint32_t)(Arg2), Arg2, a3, (uint32_t)(Arg1));
    result = MiObtainDynamicVa(result, (uint32_t)((uint32_t)((uint32_t)(Arg1))), (uint32_t)(Arg2), (uint32_t)(Arg1));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B4F44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003B4F44[BB_003B4F44]
  bb_003B4F65[BB_003B4F65]
```
