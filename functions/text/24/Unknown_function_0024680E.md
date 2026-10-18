# sub_0024680E

- RVA: `0x0024680E`–`0x00246828` (길이 `26` bytes)
- VA: `0x000000014024680E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000620EC`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00246813` → [ExAcquireSpinLockExclusiveAtDpcLevel](ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00246818` → [sub_002467B9 + 0x18](Unknown_function_002467B9.md) (`tail-transfer`)
  - `0x0024681D` → [sub_00246856 + 0xA0](Unknown_function_00246856.md) (`tail-transfer`)
  - `0x00246823` → [sub_0024663D + 0x9](Unknown_function_0024663D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024680E  C6 44 24 78 11                  mov byte ptr [rsp + 0x78], 0x11
00246813  E8 68 26 00 00                  call 0x140248e80
00246818  EB B7                           jmp 0x1402467d1
0024681A  49 3B C0                        cmp rax, r8
0024681D  0F 82 D3 00 00 00               jb 0x1402468f6
00246823  E9 1E FE FF FF                  jmp 0x140246646
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024680E(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    unsigned __int8 v_stack_p78;

    v_stack_p78 = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0024680E(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    uint8_t v_stack_p78;

    v_stack_p78 = 17;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, Arg2, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024680E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024680E[BB_0024680E]
  bb_0024681A[BB_0024681A]
  bb_00246823[BB_00246823]
  bb_0024681A -->|fallthrough| bb_00246823
```
