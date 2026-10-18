# sub_0020DF7B

- RVA: `0x0020DF7B`–`0x0020DFAC` (길이 `49` bytes)
- VA: `0x000000014020DF7B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DA50`
- 디코드: `11`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0020DFAA` → [sub_0020DFAC + 0x8](Unknown_function_0020DFAC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020DF7B  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0020DF7F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0020DF88  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0020DF8D  48 89 43 08                     mov qword ptr [rbx + 8], rax
0020DF91  41 0F B6 C7                     movzx eax, r15b
0020DF95  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0020DF9A  89 43 30                        mov dword ptr [rbx + 0x30], eax
0020DF9D  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0020DFA2  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0020DFA7  48 85 C0                        test rax, rax
0020DFAA  74 08                           je 0x14020dfb4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020DF7B(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    *(unsigned __int8 *)(v_rsi + 10) = 1;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned int *)(v_rbx + 48) = (unsigned int)((unsigned __int8)(v_r15));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0020DF7B(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11, uint64_t Arg12, int64_t Arg13)
{
    *(uint8_t *)(local_rsi + 0xA) = 1;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint32_t *)(local_rbx + 0x30) = (uint32_t)((uint8_t)(local_r15));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020DF7B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0020DF7B[BB_0020DF7B]
```
