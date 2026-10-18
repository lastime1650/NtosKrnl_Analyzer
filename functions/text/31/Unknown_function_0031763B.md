# sub_0031763B

- RVA: `0x0031763B`–`0x00317671` (길이 `54` bytes)
- VA: `0x000000014031763B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074A6C`
- 디코드: `10`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00317654` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00317648` → [sub_003178C4](Unknown_function_003178C4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031763B  49 8B 44 24 70                  mov rax, qword ptr [r12 + 0x70]
00317640  48 8B 7B 18                     mov rdi, qword ptr [rbx + 0x18]
00317644  48 83 F8 FF                     cmp rax, -1
00317648  0F 84 76 02 00 00               je 0x1403178c4
0031764E  48 8B D3                        mov rdx, rbx
00317651  48 8B CF                        mov rcx, rdi
00317654  E8 07 F8 F2 FF                  call 0x140246e60
00317659  4C 8B A4 24 88 00 00 00         mov r12, qword ptr [rsp + 0x88]
00317661  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
00317669  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0031763B(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25)
{
    __int64 result;

    result = MmUnmapLockedPages(*(unsigned __int64 *)(v_rbx + 24), v_rbx, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0031763B(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, int64_t Arg17, int64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, int64_t Arg25)
{
    int64_t result;

    result = MmUnmapLockedPages(*(uint64_t *)(local_rbx + 0x18), local_rbx, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031763B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031763B[BB_0031763B]
  bb_0031764E[BB_0031764E]
  bb_0031763B -->|fallthrough| bb_0031764E
```
