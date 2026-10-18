# sub_006E20F8

- RVA: `0x006E20F8`–`0x006E210F` (길이 `23` bytes)
- VA: `0x00000001406E20F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078190`
- 디코드: `5`개 명령, `23/23` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E20FD` → [MmCopyToCachedPage + 0xE2](../34/MmCopyToCachedPage_function_00347B44.md) (`tail-transfer`)
  - `0x006E210A` → [MmCopyToCachedPage + 0x31A](../34/MmCopyToCachedPage_function_00347B44.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E20F8  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
006E20FD  E9 24 5B C6 FF                  jmp 0x140347c26
006E2102  48 8B 03                        mov rax, qword ptr [rbx]
006E2105  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
006E210A  E9 4F 5D C6 FF                  jmp 0x140347e5e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E20F8(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
    unsigned __int64 v_stack_p48;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E20F8(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, int64_t Arg14)
{
    uint64_t v_stack_p48;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E20F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E20F8[BB_006E20F8]
  bb_006E2102[BB_006E2102]
```
