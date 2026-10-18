# IvtLegacySetDeviceSvmCapabilities

- RVA: `0x00571FB0`–`0x00571FC8` (길이 `24` bytes)
- VA: `0x0000000140571FB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00571FBD` → [IvtAllocateContextTable](../4D/IvtAllocateContextTable_function_004DE0D4.md) (function, `0x004DE0D4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00571FB0  48 83 EC 28                     sub rsp, 0x28
00571FB4  45 84 C0                        test r8b, r8b
00571FB7  75 04                           jne 0x140571fbd
00571FB9  33 C0                           xor eax, eax
00571FBB  EB 05                           jmp 0x140571fc2
00571FBD  E8 12 C1 F6 FF                  call 0x1404de0d4
00571FC2  48 83 C4 28                     add rsp, 0x28
00571FC6  C3                              ret
00571FC7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtLegacySetDeviceSvmCapabilities(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 != 0) goto loc_00571FBD;
    result = 0;
    goto loc_00571FC2;
loc_00571FBD:
    result = IvtAllocateContextTable(a1, a2, a3, a4);
loc_00571FC2:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IvtLegacySetDeviceSvmCapabilities(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 != 0) goto loc_00571FBD;
    result = 0;
    goto loc_00571FC2;
loc_00571FBD:
    result = IvtAllocateContextTable(Arg1, Arg2, Arg3, a4);
loc_00571FC2:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00571FB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00571FB0[BB_00571FB0]
  bb_00571FB9[BB_00571FB9]
  bb_00571FBD[BB_00571FBD]
  bb_00571FC2[BB_00571FC2]
  bb_00571FC7[BB_00571FC7]
  bb_00571FB0 -->|branch| bb_00571FBD
  bb_00571FB0 -->|fallthrough| bb_00571FB9
  bb_00571FB9 -->|branch| bb_00571FC2
  bb_00571FBD -->|flow| bb_00571FC2
```
