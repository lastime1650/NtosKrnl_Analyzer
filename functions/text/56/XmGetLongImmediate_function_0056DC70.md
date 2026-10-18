# XmGetLongImmediate

- RVA: `0x0056DC70`–`0x0056DCB0` (길이 `64` bytes)
- VA: `0x000000014056DC70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0056DC90` → [longjmp](../4F/longjmp_function_004FD5F0.md) (function, `0x004FD5F0`)
- `0x0056DCA3` → [x86BiosTranslateAddress](../47/x86BiosTranslateAddress_function_004736C0.md) (function, `0x004736C0`)

### Direct callers
- [XmMoveRegImmediate](../47/XmMoveRegImmediate_function_00473000.md) at `0x00473078`
- [XmGetImmediateSourceValue](../47/XmGetImmediateSourceValue_function_0047340C.md) at `0x0047344A`
- [XmAccumImmediate](../47/XmAccumImmediate_function_00473460.md) at `0x004734B0`
- [XmImmediateJump](../57/XmImmediateJump_function_005765F0.md) at `0x00576602`
- [XmLongJump](../57/XmLongJump_function_00576790.md) at `0x005767A2`
- [XmSegmentOffset](../57/XmSegmentOffset_function_00576A60.md) at `0x00576A7A`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x005789A2`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578A96`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578AA2`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578AE7`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B1F`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B2B`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B37`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B43`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B52`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3E05`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3E4D`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3E9B`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3EBA`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3ED9`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3EF8`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3F17`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3F36`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056DC70  48 83 EC 28                     sub rsp, 0x28
0056DC74  44 8B 41 14                     mov r8d, dword ptr [rcx + 0x14]
0056DC78  0F B7 51 46                     movzx edx, word ptr [rcx + 0x46]
0056DC7C  41 8D 40 03                     lea eax, [r8 + 3]
0056DC80  3B C2                           cmp eax, edx
0056DC82  76 12                           jbe 0x14056dc96
0056DC84  48 81 C1 A0 00 00 00            add rcx, 0xa0
0056DC8B  BA 0E 00 00 00                  mov edx, 0xe
0056DC90  E8 5B F9 F8 FF                  call 0x1404fd5f0
0056DC95  CC                              int3
0056DC96  66 83 41 14 04                  add word ptr [rcx + 0x14], 4
0056DC9B  41 0F B7 D0                     movzx edx, r8w
0056DC9F  0F B7 49 3A                     movzx ecx, word ptr [rcx + 0x3a]
0056DCA3  E8 18 5A F0 FF                  call 0x1404736c0
0056DCA8  8B 00                           mov eax, dword ptr [rax]
0056DCAA  48 83 C4 28                     add rsp, 0x28
0056DCAE  C3                              ret
0056DCAF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmGetLongImmediate(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(a1 + 20)) + 3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)) + 3)) >= = ((unsigned int)(*(unsigned __int16 *)(a1 + 70)))) {
        a1 = (a1) + (160);
        a2 = 14;
        result = longjmp(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 20)), a4);
    }
    result = x86BiosTranslateAddress(*(unsigned __int16 *)(a1 + 58), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1 + 20))), (unsigned int)(*(unsigned int *)(a1 + 20)), a4);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(result));
}
```

## 5. (Beta) C Style

```c
int64_t XmGetLongImmediate(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x14)) + 3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)) + 3)) >= = ((uint32_t)(*(uint16_t *)(arg1 + 0x46)))) {
        Arg1 = (Arg1) + (160);
        a2 = 14;
        result = longjmp(Arg1, a2, (uint32_t)(*(uint32_t *)(arg1 + 0x14)), a4);
    }
    result = x86BiosTranslateAddress(*(uint16_t *)(arg1 + 0x3A), (uint16_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))), (uint32_t)(*(uint32_t *)(arg1 + 0x14)), a4);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(result));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x46` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056DC70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056DC70[BB_0056DC70]
  bb_0056DC84[BB_0056DC84]
  bb_0056DC96[BB_0056DC96]
  bb_0056DCAF[BB_0056DCAF]
  bb_0056DC70 -->|branch| bb_0056DC96
  bb_0056DC70 -->|fallthrough| bb_0056DC84
  bb_0056DC84 -->|flow| bb_0056DC96
```
