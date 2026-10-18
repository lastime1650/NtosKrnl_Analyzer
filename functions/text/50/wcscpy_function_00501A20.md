# wcscpy

- RVA: `0x00501A20`–`0x00501A5A` (길이 `58` bytes)
- VA: `0x0000000140501A20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `17`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00501A33` → [wcslen](wcslen_function_00501BA0.md) (function, `0x00501BA0`)
- `0x00501A46` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [wcscat](wcscat_function_005019E0.md) at `0x005019FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00501A20  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00501A25  57                              push rdi
00501A26  48 83 EC 20                     sub rsp, 0x20
00501A2A  48 8B F9                        mov rdi, rcx
00501A2D  48 8B DA                        mov rbx, rdx
00501A30  48 8B CA                        mov rcx, rdx
00501A33  E8 68 01 00 00                  call 0x140501ba0
00501A38  48 8B D3                        mov rdx, rbx
00501A3B  48 8B CF                        mov rcx, rdi
00501A3E  4C 8D 04 45 02 00 00 00         lea r8, [rax*2 + 2]
00501A46  E8 F5 4D 1C 00                  call 0x1406c6840
00501A4B  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00501A50  48 8B C7                        mov rax, rdi
00501A53  48 83 C4 20                     add rsp, 0x20
00501A57  5F                              pop rdi
00501A58  C3                              ret
00501A59  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wcscpy(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = wcslen(a2, a2, a3, a4);
    result = memcpy(a1, a2, result * 2 + 2, a4);
    v_rsp = (v_rsp) + (32);
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t wcscpy(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = wcslen(Arg2, Arg2, a3, a4);
    result = memcpy(Arg1, Arg2, result * 2 + 2, a4);
    local_rsp = (local_rsp) + (32);
    return Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00501A20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00501A20[BB_00501A20]
  bb_00501A59[BB_00501A59]
```
