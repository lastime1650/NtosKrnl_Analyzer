# sub_00207282

- RVA: `0x00207282`–`0x002072AC` (길이 `42` bytes)
- VA: `0x0000000140207282`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D134`
- 디코드: `9`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00207291` → [KxWaitForSpinLockAndAcquire](KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x002072A2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00207288` → [sub_00207169 + 0x49](Unknown_function_00207169.md) (`tail-transfer`)
  - `0x00207296` → [sub_00207169 + 0x49](Unknown_function_00207169.md) (`tail-transfer`)
  - `0x002072A7` → [sub_00207169 + 0x26](Unknown_function_00207169.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00207282  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00207288  0F 83 24 FF FF FF               jae 0x1402071b2
0020728E  48 8B CB                        mov rcx, rbx
00207291  E8 2A 13 00 00                  call 0x1402085c0
00207296  E9 17 FF FF FF                  jmp 0x1402071b2
0020729B  0F B6 D0                        movzx edx, al
0020729E  40 0F B6 CE                     movzx ecx, sil
002072A2  E8 55 E4 2E 00                  call 0x1404f56fc
002072A7  E9 E3 FE FF FF                  jmp 0x14020718f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00207282(void)
{
    __int64 result;

    result = KxWaitForSpinLockAndAcquire(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00207282(void)
{
    int64_t result;

    result = KxWaitForSpinLockAndAcquire(local_rbx, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00207282&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00207282[BB_00207282]
  bb_0020728E[BB_0020728E]
  bb_0020729B[BB_0020729B]
  bb_00207282 -->|fallthrough| bb_0020728E
```
