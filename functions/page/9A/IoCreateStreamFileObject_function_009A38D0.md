# IoCreateStreamFileObject

- RVA: `0x009A38D0`–`0x009A390D` (길이 `61` bytes)
- VA: `0x00000001409A38D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082420`
- 디코드: `16`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A38FD` → [IoCreateStreamFileObjectEx2](IoCreateStreamFileObjectEx2_function_009A5900.md) (function, `0x009A5900`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A38D0  48 8B C4                        mov rax, rsp
009A38D3  48 83 EC 48                     sub rsp, 0x48
009A38D7  48 83 60 18 00                  and qword ptr [rax + 0x18], 0
009A38DC  4C 8D 48 18                     lea r9, [rax + 0x18]
009A38E0  48 83 60 D8 00                  and qword ptr [rax - 0x28], 0
009A38E5  0F 57 C0                        xorps xmm0, xmm0
009A38E8  4C 8B C2                        mov r8, rdx
009A38EB  48 8B D1                        mov rdx, rcx
009A38EE  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
009A38F2  48 8D 48 E8                     lea rcx, [rax - 0x18]
009A38F6  C7 40 E8 10 00 01 00            mov dword ptr [rax - 0x18], 0x10010
009A38FD  E8 FE 1F 00 00                  call 0x1409a5900
009A3902  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009A3907  48 83 C4 48                     add rsp, 0x48
009A390B  C3                              ret
009A390C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoCreateStreamFileObject(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_rsp = (v_rsp) - (72);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    *(unsigned int *)(v_rsp - 24) = 0x10010ULL;
    result = IoCreateStreamFileObjectEx2(v_rsp - 24, a1, a2, v_rsp + 24);
    v_rsp = (v_rsp) + (72);
    return v_stack_p18;
}
```

## 5. (Beta) C Style

```c
int64_t IoCreateStreamFileObject(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p18;

    local_rsp = (local_rsp) - (72);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x18) = 0x10010ULL;
    result = IoCreateStreamFileObjectEx2(local_rsp - 24, Arg1, Arg2, local_rsp + 24);
    local_rsp = (local_rsp) + (72);
    return v_stack_p18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A38D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A38D0[BB_009A38D0]
  bb_009A390C[BB_009A390C]
```
