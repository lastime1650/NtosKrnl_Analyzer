# sub_00B2C56E

- RVA: `0x00B2C56E`–`0x00B2C588` (길이 `26` bytes)
- VA: `0x0000000140B2C56E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000992E8`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2C570` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B2C57D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B2C570` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B2C57D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B2C576` → [PnpPrepareDriverLoading + 0xB3](../99/PnpPrepareDriverLoading_function_00996CC8.md) (`tail-transfer`)
  - `0x00B2C583` → [PnpPrepareDriverLoading + 0x149](../99/PnpPrepareDriverLoading_function_00996CC8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2C56E  33 D2                           xor edx, edx
00B2C570  E8 FB 62 05 00                  call 0x140b82870
00B2C575  90                              nop
00B2C576  E9 00 A8 E6 FF                  jmp 0x140996d7b
00B2C57B  33 D2                           xor edx, edx
00B2C57D  E8 EE 62 05 00                  call 0x140b82870
00B2C582  90                              nop
00B2C583  E9 89 A8 E6 FF                  jmp 0x140996e11
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2C56E(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B2C56E(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2C56E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2C56E[BB_00B2C56E]
  bb_00B2C57B[BB_00B2C57B]
```
