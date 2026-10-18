# IopGetRegistryBoolValue

- RVA: `0x00598E84`–`0x00598E9C` (길이 `24` bytes)
- VA: `0x0000000140598E84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00598E88` → [IopGetRegistryULongValue](IopGetRegistryULongValue_function_00598EA4.md) (function, `0x00598EA4`)

### Direct callers
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C934`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C956`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C976`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C998`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C9BA`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C9DC`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059C9FE`
- [IopLiveDumpInitRegistrySettings](IopLiveDumpInitRegistrySettings_function_0059C8A4.md) at `0x0059CA20`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00598E84  48 83 EC 28                     sub rsp, 0x28
00598E88  E8 17 00 00 00                  call 0x140598ea4
00598E8D  33 C9                           xor ecx, ecx
00598E8F  85 C0                           test eax, eax
00598E91  0F 95 C1                        setne cl
00598E94  8B C1                           mov eax, ecx
00598E96  48 83 C4 28                     add rsp, 0x28
00598E9A  C3                              ret
00598E9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetRegistryBoolValue(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = IopGetRegistryULongValue(a1, a2, a3, a4);
    a1 = 0;
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t IopGetRegistryBoolValue(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = IopGetRegistryULongValue(Arg1, a2, a3, a4);
    Arg1 = 0;
    Arg1 = ((uint32_t)(result) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00598E84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00598E84[BB_00598E84]
  bb_00598E9B[BB_00598E9B]
```
