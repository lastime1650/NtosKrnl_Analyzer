# KeRemoveQueue

- RVA: `0x00467700`–`0x00467732` (길이 `50` bytes)
- VA: `0x0000000140467700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00467722` → [KeRemoveQueueEx](../20/KeRemoveQueueEx_function_0020BD30.md) (function, `0x0020BD30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00467700  48 83 EC 38                     sub rsp, 0x38
00467704  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
0046770A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0046770F  4D 8B C8                        mov r9, r8
00467712  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0046771A  45 33 C0                        xor r8d, r8d
0046771D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00467722  E8 09 46 DA FF                  call 0x14020bd30
00467727  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0046772C  48 83 C4 38                     add rsp, 0x38
00467730  C3                              ret
00467731  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRemoveQueue(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    v_stack_m10 = 1;
    a3 = 0;
    v_stack_m18 = v_stack_p20;
    result = KeRemoveQueueEx(a1, a2, a3, a3);
    v_rsp = (v_rsp) + (56);
    return v_stack_p20;
}
```

## 5. (Beta) C Style

```c
int64_t KeRemoveQueue(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    v_stack_m10 = 1;
    Arg3 = 0;
    v_stack_m18 = v_stack_p20;
    result = KeRemoveQueueEx(Arg1, Arg2, Arg3, Arg3);
    local_rsp = (local_rsp) + (56);
    return v_stack_p20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00467700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00467700[BB_00467700]
  bb_00467731[BB_00467731]
```
