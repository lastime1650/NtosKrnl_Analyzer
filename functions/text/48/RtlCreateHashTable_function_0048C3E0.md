# RtlCreateHashTable

- RVA: `0x0048C3E0`–`0x0048C3FA` (길이 `26` bytes)
- VA: `0x000000014048C3E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048C3EF` → [RtlpCreateHashTable](RtlpCreateHashTable_function_0048C400.md) (function, `0x0048C400`)

### Direct callers
- [SepInitializeLowBoxNumberTable](../../page/7A/SepInitializeLowBoxNumberTable_function_007A31E4.md) at `0x007A3207`
- [SepInitializeSharedSidMap](../../page/7A/SepInitializeSharedSidMap_function_007A3270.md) at `0x007A328C`
- [SepSetTokenCachedHandles](../../page/9A/SepSetTokenCachedHandles_function_009A939C.md) at `0x009A95A3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048C3E0  48 83 EC 28                     sub rsp, 0x28
0048C3E4  45 8B C8                        mov r9d, r8d
0048C3E7  44 8B C2                        mov r8d, edx
0048C3EA  BA 80 00 00 00                  mov edx, 0x80
0048C3EF  E8 0C 00 00 00                  call 0x14048c400
0048C3F4  48 83 C4 28                     add rsp, 0x28
0048C3F8  C3                              ret
0048C3F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCreateHashTable(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpCreateHashTable(a1, 128, (unsigned int)(a2), (unsigned int)(a3));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCreateHashTable(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpCreateHashTable(Arg1, 128, (uint32_t)(Arg2), (uint32_t)(Arg3));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048C3E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048C3E0[BB_0048C3E0]
  bb_0048C3F9[BB_0048C3F9]
```
