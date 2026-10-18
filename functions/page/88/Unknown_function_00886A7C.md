# sub_00886A7C

- RVA: `0x00886A7C`–`0x00886AA0` (길이 `36` bytes)
- VA: `0x0000000140886A7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007CB00`
- 디코드: `8`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00886A90` → [MiHonorRangeStraddleRequirement](../../text/46/MiHonorRangeStraddleRequirement_function_00462818.md) (function, `0x00462818`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00886A90` → [MiHonorRangeStraddleRequirement](../../text/46/MiHonorRangeStraddleRequirement_function_00462818.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00886A9B` → [sub_00886963 + 0x84](Unknown_function_00886963.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00886A7C  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00886A84  41 B9 01 00 00 00               mov r9d, 1
00886A8A  4C 8B C5                        mov r8, rbp
00886A8D  49 8B CC                        mov rcx, r12
00886A90  E8 83 BD BD FF                  call 0x140462818
00886A95  4C 8B E0                        mov r12, rax
00886A98  4D 23 E6                        and r12, r14
00886A9B  E9 47 FF FF FF                  jmp 0x1408869e7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00886A7C(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19)
{
    __int64 result;
    __int64 v_r12;

    result = MiHonorRangeStraddleRequirement(v_r12, a19, v_rbp, 1);
    v_r12 = (result) & (v_r14);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00886A7C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, int64_t Arg19)
{
    int64_t result;
    int64_t local_r12;

    result = MiHonorRangeStraddleRequirement(local_r12, Arg19, local_rbp, 1);
    local_r12 = (result) & (local_r14);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00886A7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00886A7C[BB_00886A7C]
```
