# sub_00B1ADAA

- RVA: `0x00B1ADAA`–`0x00B1ADD2` (길이 `40` bytes)
- VA: `0x0000000140B1ADAA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000832F8`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1ADAE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B1ADC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B1ADAE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00B1ADC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B1ADB4` → [ExpWnfPopulateStateData + 0xF6](../8B/ExpWnfPopulateStateData_function_008BF354.md) (`tail-transfer`)
  - `0x00B1ADCD` → [ExpWnfPopulateStateData + 0x65](../8B/ExpWnfPopulateStateData_function_008BF354.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1ADAA  49 8D 4F 08                     lea rcx, [r15 + 8]
00B1ADAE  E8 4D 68 7C FF                  call 0x1402e1600
00B1ADB3  90                              nop
00B1ADB4  E9 91 46 DA FF                  jmp 0x1408bf44a
00B1ADB9  BF 01 00 00 C0                  mov edi, 0xc0000001
00B1ADBE  BA 57 6E 66 20                  mov edx, 0x20666e57
00B1ADC3  48 8B CB                        mov rcx, rbx
00B1ADC6  E8 A5 7A 06 00                  call 0x140b82870
00B1ADCB  8B C7                           mov eax, edi
00B1ADCD  E9 E7 45 DA FF                  jmp 0x1408bf3b9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1ADAA(void)
{
    __int64 result;

    result = KeAbPostRelease(v_r15 + 8, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B1ADAA(void)
{
    int64_t result;

    result = KeAbPostRelease(local_r15 + 8, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1ADAA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1ADAA[BB_00B1ADAA]
  bb_00B1ADB9[BB_00B1ADB9]
```
