# sub_003ED642

- RVA: `0x003ED642`–`0x003ED675` (길이 `51` bytes)
- VA: `0x00000001403ED642`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096904`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003ED656` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003ED66C` → [sub_003ED675](Unknown_function_003ED675.md) (`tail-transfer`)
  - `0x003ED673` → [ObFastDereferenceObject + 0x44](ObFastDereferenceObject_function_003ED5F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003ED642  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003ED647  74 12                           je 0x1403ed65b
003ED649  33 D2                           xor edx, edx
003ED64B  48 8D 4B D0                     lea rcx, [rbx - 0x30]
003ED64F  45 8B CA                        mov r9d, r10d
003ED652  44 8D 42 01                     lea r8d, [rdx + 1]
003ED656  E8 89 33 E2 FF                  call 0x1402109e4
003ED65B  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
003ED662  F0 48 0F C1 43 D0               lock xadd qword ptr [rbx - 0x30], rax
003ED668  48 83 E8 01                     sub rax, 1
003ED66C  7E 07                           jle 0x1403ed675
003ED66E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
003ED673  EB BF                           jmp 0x1403ed634
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003ED642(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    unsigned __int64 v_stack_p40;

    v_stack_p40 = v_rdi;
    if (!(condition_is_equal)) {
        a2 = 0;
        a1 = v_rbx - 48;
        a4 = (unsigned int)(v_r10);
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
}
```

## 5. (Beta) C Style

```c
int64_t sub_003ED642(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t result;
    uint64_t v_stack_p40;

    v_stack_p40 = local_rdi;
    if (!(condition_is_equal)) {
        Arg2 = 0;
        Arg1 = local_rbx - 48;
        Arg4 = (uint32_t)(local_r10);
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ED642&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003ED642[BB_003ED642]
  bb_003ED649[BB_003ED649]
  bb_003ED65B[BB_003ED65B]
  bb_003ED66E[BB_003ED66E]
  bb_003ED642 -->|branch| bb_003ED65B
  bb_003ED642 -->|fallthrough| bb_003ED649
  bb_003ED649 -->|flow| bb_003ED65B
  bb_003ED65B -->|fallthrough| bb_003ED66E
```
