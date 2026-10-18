# sub_0027CCA5

- RVA: `0x0027CCA5`–`0x0027CCDA` (길이 `53` bytes)
- VA: `0x000000014027CCA5`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000661BC`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0027CCC2` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0027CCD0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0027CCB5` → [sub_0027CC13 + 0x62](Unknown_function_0027CC13.md) (`tail-transfer`)
  - `0x0027CCC7` → [sub_0027CC13 + 0x62](Unknown_function_0027CC13.md) (`tail-transfer`)
  - `0x0027CCD5` → [sub_0027CC13 + 0x43](Unknown_function_0027CC13.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0027CCA5  0F 0D 0F                        prefetchw byte ptr [rdi]
0027CCA8  8B 07                           mov eax, dword ptr [rdi]
0027CCAA  0F BA F0 1F                     btr eax, 0x1f
0027CCAE  8D 48 01                        lea ecx, [rax + 1]
0027CCB1  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
0027CCB5  74 BE                           je 0x14027cc75
0027CCB7  85 C0                           test eax, eax
0027CCB9  79 F3                           jns 0x14027ccae
0027CCBB  40 0F B6 D6                     movzx edx, sil
0027CCBF  48 8B CF                        mov rcx, rdi
0027CCC2  E8 B9 56 0E 00                  call 0x140362380
0027CCC7  EB AC                           jmp 0x14027cc75
0027CCC9  0F B6 D1                        movzx edx, cl
0027CCCC  40 0F B6 CE                     movzx ecx, sil
0027CCD0  E8 27 8A 27 00                  call 0x1404f56fc
0027CCD5  E9 7C FF FF FF                  jmp 0x14027cc56
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0027CCA5(void)
{
    __int64 result;

loc_0027CCAE:
    if (!sign_flag) goto loc_0027CCAE;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rdi, (unsigned __int8)(v_rsi), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0027CCA5(void)
{
    int64_t result;

loc_0027CCAE:
    if (!sign_flag) goto loc_0027CCAE;
    result = ExpWaitForSpinLockSharedAndAcquire(local_rdi, (uint8_t)(local_rsi), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027CCA5&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0027CCA5[BB_0027CCA5]
  bb_0027CCAE[BB_0027CCAE]
  bb_0027CCB7[BB_0027CCB7]
  bb_0027CCBB[BB_0027CCBB]
  bb_0027CCC9[BB_0027CCC9]
  bb_0027CCA5 -->|flow| bb_0027CCAE
  bb_0027CCAE -->|fallthrough| bb_0027CCB7
  bb_0027CCB7 -->|branch| bb_0027CCAE
  bb_0027CCB7 -->|fallthrough| bb_0027CCBB
```
