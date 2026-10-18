# HvlpInitializeHvCrashdumpPhase2

- RVA: `0x0058C01C`–`0x0058C0A7` (길이 `139` bytes)
- VA: `0x000000014058C01C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `27`개 명령, `139/139` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0058C02C` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C03D` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C04E` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C05F` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C079` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C08A` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0058C09C` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)

### Direct callers
- [HvlPhase2Initialize](HvlPhase2Initialize_function_00583EA0.md) at `0x00583FF0`

### Static image references
- `0x0058C025` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x0058C036` → RVA `0x00FC6AD8` (`ALMOSTRO`; read)
- `0x0058C047` → RVA `0x00FC6C98` (`ALMOSTRO`; read)
- `0x0058C058` → RVA `0x00F8ECC0` (`.data`; read)
- `0x0058C064` → RVA `0x00F8ECAC` (`.data`; read)
- `0x0058C072` → RVA `0x00F8ECB8` (`.data`; read)
- `0x0058C083` → RVA `0x00F8ECB0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058C01C  48 83 EC 28                     sub rsp, 0x28
0058C020  BA 04 00 00 00                  mov edx, 4
0058C025  48 8D 0D 64 AA A3 00            lea rcx, [rip + 0xa3aa64]
0058C02C  E8 43 C3 E9 FF                  call 0x140428374
0058C031  BA 04 00 00 00                  mov edx, 4
0058C036  48 8D 0D 9B AA A3 00            lea rcx, [rip + 0xa3aa9b]
0058C03D  E8 32 C3 E9 FF                  call 0x140428374
0058C042  BA 04 00 00 00                  mov edx, 4
0058C047  48 8D 0D 4A AC A3 00            lea rcx, [rip + 0xa3ac4a]
0058C04E  E8 21 C3 E9 FF                  call 0x140428374
0058C053  BA 00 01 00 00                  mov edx, 0x100
0058C058  48 8D 0D 61 2C A0 00            lea rcx, [rip + 0xa02c61]
0058C05F  E8 10 C3 E9 FF                  call 0x140428374
0058C064  80 3D 41 2C A0 00 00            cmp byte ptr [rip + 0xa02c41], 0
0058C06B  74 34                           je 0x14058c0a1
0058C06D  BA 04 00 00 00                  mov edx, 4
0058C072  48 8D 0D 3F 2C A0 00            lea rcx, [rip + 0xa02c3f]
0058C079  E8 F6 C2 E9 FF                  call 0x140428374
0058C07E  BA 08 00 00 00                  mov edx, 8
0058C083  48 8D 0D 26 2C A0 00            lea rcx, [rip + 0xa02c26]
0058C08A  E8 E5 C2 E9 FF                  call 0x140428374
0058C08F  8B 15 23 2C A0 00               mov edx, dword ptr [rip + 0xa02c23]
0058C095  48 8B 0D 14 2C A0 00            mov rcx, qword ptr [rip + 0xa02c14]
0058C09C  E8 D3 C2 E9 FF                  call 0x140428374
0058C0A1  48 83 C4 28                     add rsp, 0x28
0058C0A5  C3                              ret
0058C0A6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpInitializeHvCrashdumpPhase2(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = IoAddTriageDumpDataBlock(v_rip + 10725988, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10726043, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10726474, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10497121, 256, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 10497089)) != 0) {
        a2 = 4;
        a1 = v_rip + 10497087;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = 8;
        a1 = v_rip + 10497062;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(unsigned int *)(v_rip + 10497059);
        a1 = *(unsigned __int64 *)(v_rip + 10497044);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HvlpInitializeHvCrashdumpPhase2(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = IoAddTriageDumpDataBlock(v_rip + 10725988, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10726043, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10726474, 4, a3, a4);
    result = IoAddTriageDumpDataBlock(v_rip + 10497121, 256, a3, a4);
    if ((*(uint8_t *)(v_rip + 0xA02C41)) != 0) {
        a2 = 4;
        a1 = v_rip + 10497087;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = 8;
        a1 = v_rip + 10497062;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(uint32_t *)(v_rip + 0xA02C23);
        a1 = *(uint64_t *)(v_rip + 0xA02C14);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058C01C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058C01C[BB_0058C01C]
  bb_0058C06D[BB_0058C06D]
  bb_0058C0A1[BB_0058C0A1]
  bb_0058C0A6[BB_0058C0A6]
  bb_0058C01C -->|branch| bb_0058C0A1
  bb_0058C01C -->|fallthrough| bb_0058C06D
  bb_0058C06D -->|flow| bb_0058C0A1
```
