# sub_0084D46C

- RVA: `0x0084D46C`–`0x0084D499` (길이 `45` bytes)
- VA: `0x000000014084D46C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000699E0`
- 디코드: `10`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084D47D` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0084D47D` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0084D488` → [sub_0084D0A2 + 0xBF](Unknown_function_0084D0A2.md) (`tail-transfer`)
  - `0x0084D494` → [sub_0084D349](Unknown_function_0084D349.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0084D46C  8B D0                           mov edx, eax
0084D46E  B9 00 01 00 00                  mov ecx, 0x100
0084D473  48 C1 E2 03                     shl rdx, 3
0084D477  41 B8 43 4D 36 35               mov r8d, 0x35364d43
0084D47D  E8 82 00 B8 FF                  call 0x1403cd504
0084D482  48 8B C8                        mov rcx, rax
0084D485  48 85 C0                        test rax, rax
0084D488  0F 85 D3 FC FF FF               jne 0x14084d161
0084D48E  41 BD 9A 00 00 C0               mov r13d, 0xc000009a
0084D494  E9 B0 FE FF FF                  jmp 0x14084d349
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0084D46C(void)
{
    __int64 result;

    a2 = ((unsigned int)((unsigned int)(result))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), a4);
}
```

## 5. (Beta) C Style

```c
void sub_0084D46C(void)
{
    int64_t result;

    a2 = ((uint32_t)((uint32_t)(result))) << (3);
    result = CmpAllocatePool(256, a2, (uint32_t)(0x35364D43ULL), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084D46C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084D46C[BB_0084D46C]
  bb_0084D48E[BB_0084D48E]
  bb_0084D46C -->|fallthrough| bb_0084D48E
```
