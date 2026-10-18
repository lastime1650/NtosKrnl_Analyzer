# sub_00B806E6

- RVA: `0x00B806E6`–`0x00B80710` (길이 `42` bytes)
- VA: `0x0000000140B806E6`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ABF70`
- 디코드: `12`개 명령, `42/42` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B806E6  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00B806EB  49 8B C6                        mov rax, r14
00B806EE  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00B806F3  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00B806F8  C7 47 18 00 00 00 00            mov dword ptr [rdi + 0x18], 0
00B806FF  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00B80704  48 83 C4 20                     add rsp, 0x20
00B80708  41 5F                           pop r15
00B8070A  41 5E                           pop r14
00B8070C  41 5C                           pop r12
00B8070E  C3                              ret
00B8070F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B806E6(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 v_rsp;

    *(unsigned int *)(v_rdi + 24) = 0;
    v_rsp = (v_rsp) + (32);
    return v_r14;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B806E6(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t local_rsp;

    *(uint32_t *)(local_rdi + 0x18) = 0;
    local_rsp = (local_rsp) + (32);
    return local_r14;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B806E6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B806E6[BB_00B806E6]
  bb_00B8070F[BB_00B8070F]
```
