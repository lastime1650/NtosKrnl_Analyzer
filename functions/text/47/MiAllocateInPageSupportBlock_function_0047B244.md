# MiAllocateInPageSupportBlock

- RVA: `0x0047B244`–`0x0047B277` (길이 `51` bytes)
- VA: `0x000000014047B244`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0047B26C` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)

### Direct callers
- [MiInitializePageFaultResources](../67/MiInitializePageFaultResources_function_0067E490.md) at `0x0067E4F9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047B244  48 83 EC 28                     sub rsp, 0x28
0047B248  8B C2                           mov eax, edx
0047B24A  F7 D9                           neg ecx
0047B24C  B9 40 00 00 00                  mov ecx, 0x40
0047B251  41 B8 4D 6D 49 6E               mov r8d, 0x6e496d4d
0047B257  48 1B D2                        sbb rdx, rdx
0047B25A  48 81 E2 80 F8 FF FF            and rdx, 0xfffffffffffff880
0047B261  48 81 C2 40 09 00 00            add rdx, 0x940
0047B268  48 0F AF D0                     imul rdx, rax
0047B26C  E8 CF 02 EE FF                  call 0x14035b540
0047B271  48 83 C4 28                     add rsp, 0x28
0047B275  C3                              ret
0047B276  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateInPageSupportBlock(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)(-(a1));
    a2 = (a2) & (0xFFFFFFFFFFFFF880ULL);
    a2 = (a2) + (0x940ULL);
    a2 = (a2) * ((unsigned int)((unsigned int)(a2)));
    result = MiAllocatePool(64, a2, (unsigned int)(0x6E496D4DULL), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateInPageSupportBlock(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)(-(Arg1));
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF880ULL);
    Arg2 = (Arg2) + (0x940ULL);
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg2)));
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x6E496D4DULL), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047B244&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047B244[BB_0047B244]
  bb_0047B276[BB_0047B276]
```
