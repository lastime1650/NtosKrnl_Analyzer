# PopNetNonCompliantDeviceUpdate

- RVA: `0x00768CB0`–`0x00768D00` (길이 `80` bytes)
- VA: `0x0000000140768CB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `25`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00768CDE` → [PopNetClearConnectivityConstraint](../AD/PopNetClearConnectivityConstraint_function_00ADB124.md) (function, `0x00ADB124`)
- `0x00768CF5` → [PopNetSetConnectivityConstraint](PopNetSetConnectivityConstraint_function_00768E90.md) (function, `0x00768E90`)

### Direct callers
- [PopPdcCsDeviceNotification](../AA/PopPdcCsDeviceNotification_function_00AA1B28.md) at `0x00AA1CCA`

### Static image references
- `0x00768CB8` → RVA `0x00E679D4` (`.data`; read)
- `0x00768CC0` → RVA `0x00F086FC` (`.data`; read)
- `0x00768CD1` → RVA `0x00F086FC` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00768CB0  48 83 EC 28                     sub rsp, 0x28
00768CB4  85 D2                           test edx, edx
00768CB6  75 08                           jne 0x140768cc0
00768CB8  39 15 16 ED 6F 00               cmp dword ptr [rip + 0x6fed16], edx
00768CBE  75 3A                           jne 0x140768cfa
00768CC0  8B 05 36 FA 79 00               mov eax, dword ptr [rip + 0x79fa36]
00768CC6  84 C9                           test cl, cl
00768CC8  75 1B                           jne 0x140768ce5
00768CCA  85 C0                           test eax, eax
00768CCC  74 2C                           je 0x140768cfa
00768CCE  83 C0 FF                        add eax, -1
00768CD1  89 05 25 FA 79 00               mov dword ptr [rip + 0x79fa25], eax
00768CD7  75 21                           jne 0x140768cfa
00768CD9  B9 03 00 00 00                  mov ecx, 3
00768CDE  E8 41 24 37 00                  call 0x140adb124
00768CE3  EB 15                           jmp 0x140768cfa
00768CE5  FF C0                           inc eax
00768CE7  89 05 0F FA 79 00               mov dword ptr [rip + 0x79fa0f], eax
00768CED  83 F8 01                        cmp eax, 1
00768CF0  75 08                           jne 0x140768cfa
00768CF2  8D 48 02                        lea ecx, [rax + 2]
00768CF5  E8 96 01 00 00                  call 0x140768e90
00768CFA  48 83 C4 28                     add rsp, 0x28
00768CFE  C3                              ret
00768CFF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopNetNonCompliantDeviceUpdate(unsigned __int8 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != 0) goto loc_00768CC0;
    if ((*(unsigned int *)(v_rip + 7335190)) != a2) goto loc_00768CFA;
loc_00768CC0:
    if (a1 != 0) goto loc_00768CE5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7993910))) == 0) goto loc_00768CFA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7993910))) + (-1));
    *(unsigned int *)(v_rip + 7993893) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_00768CFA;
    result = PopNetClearConnectivityConstraint(3, a2, a3, a4);
    goto loc_00768CFA;
loc_00768CE5:
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(v_rip + 7993871) = (unsigned int)(result);
    if (((unsigned int)(result)) == 1) {
        a1 = result + 2;
        result = PopNetSetConnectivityConstraint(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopNetNonCompliantDeviceUpdate(uint8_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != 0) goto loc_00768CC0;
    if ((*(uint32_t *)(v_rip + 0x6FED16)) != Arg2) goto loc_00768CFA;
loc_00768CC0:
    if (Arg1 != 0) goto loc_00768CE5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x79FA36))) == 0) goto loc_00768CFA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x79FA36))) + (-1));
    *(uint32_t *)(v_rip + 0x79FA25) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_00768CFA;
    result = PopNetClearConnectivityConstraint(3, Arg2, a3, a4);
    goto loc_00768CFA;
loc_00768CE5:
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(v_rip + 0x79FA0F) = (uint32_t)(result);
    if (((uint32_t)(result)) == 1) {
        Arg1 = result + 2;
        result = PopNetSetConnectivityConstraint(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00768CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00768CB0[BB_00768CB0]
  bb_00768CB8[BB_00768CB8]
  bb_00768CC0[BB_00768CC0]
  bb_00768CCA[BB_00768CCA]
  bb_00768CCE[BB_00768CCE]
  bb_00768CD9[BB_00768CD9]
  bb_00768CE5[BB_00768CE5]
  bb_00768CF2[BB_00768CF2]
  bb_00768CFA[BB_00768CFA]
  bb_00768CFF[BB_00768CFF]
  bb_00768CB0 -->|branch| bb_00768CC0
  bb_00768CB0 -->|fallthrough| bb_00768CB8
  bb_00768CB8 -->|branch| bb_00768CFA
  bb_00768CB8 -->|fallthrough| bb_00768CC0
  bb_00768CC0 -->|branch| bb_00768CE5
  bb_00768CC0 -->|fallthrough| bb_00768CCA
  bb_00768CCA -->|branch| bb_00768CFA
  bb_00768CCA -->|fallthrough| bb_00768CCE
  bb_00768CCE -->|branch| bb_00768CFA
  bb_00768CCE -->|fallthrough| bb_00768CD9
  bb_00768CD9 -->|branch| bb_00768CFA
  bb_00768CE5 -->|branch| bb_00768CFA
  bb_00768CE5 -->|fallthrough| bb_00768CF2
  bb_00768CF2 -->|flow| bb_00768CFA
```
