# sub_003FF05D

- RVA: `0x003FF05D`–`0x003FF07D` (길이 `32` bytes)
- VA: `0x00000001403FF05D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099FD8`
- 디코드: `13`개 명령, `32/32` bytes 표시
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
003FF05D  48 83 C3 20                     add rbx, 0x20
003FF061  83 F8 01                        cmp eax, 1
003FF064  48 0F 44 F3                     cmove rsi, rbx
003FF068  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
003FF06D  48 8B C6                        mov rax, rsi
003FF070  48 83 C4 20                     add rsp, 0x20
003FF074  5F                              pop rdi
003FF075  5E                              pop rsi
003FF076  5D                              pop rbp
003FF077  C3                              ret
003FF078  CC                              int3
003FF079  8B C6                           mov eax, esi
003FF07B  EB E0                           jmp 0x1403ff05d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003FF05D(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;

    v_rbx = (v_rbx) + (32);
    if (((unsigned int)(result)) == 1) { v_rsi = v_rbx; }
    v_rsp = (v_rsp) + (32);
    return v_rsi;
}
```

## 5. (Beta) C Style

```c
int64_t sub_003FF05D(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11)
{
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;

    local_rbx = (local_rbx) + (32);
    if (((uint32_t)(result)) == 1) { local_rsi = local_rbx; }
    local_rsp = (local_rsp) + (32);
    return local_rsi;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FF05D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FF05D[BB_003FF05D]
  bb_003FF078[BB_003FF078]
  bb_003FF078 -->|branch| bb_003FF05D
```
