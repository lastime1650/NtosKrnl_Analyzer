# VrpAllocateKeyContext

- RVA: `0x00937204`–`0x0093724E` (길이 `74` bytes)
- VA: `0x0000000140937204`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `21`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00937221` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00937236` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)

### Direct callers
- [VrpPostOpenOrCreate](VrpPostOpenOrCreate_function_00936510.md) at `0x009365C2`
- [VrpPostOpenOrCreate](VrpPostOpenOrCreate_function_00936510.md) at `0x009366C5`
- [VrpHandleIoctlInitializeJobForVreg](VrpHandleIoctlInitializeJobForVreg_function_00937254.md) at `0x00937427`
- [sub_00B4588A](../B4/Unknown_function_00B4588A.md) at `0x00B45E37`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00937221` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00937236` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00937204  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00937209  57                              push rdi
0093720A  48 83 EC 20                     sub rsp, 0x20
0093720E  48 8B F9                        mov rdi, rcx
00937211  BA 30 00 00 00                  mov edx, 0x30
00937216  B9 00 01 00 00                  mov ecx, 0x100
0093721B  41 B8 56 52 65 67               mov r8d, 0x67655256
00937221  E8 CA AE 24 00                  call 0x140b820f0
00937226  48 8B D8                        mov rbx, rax
00937229  48 85 C0                        test rax, rax
0093722C  74 11                           je 0x14093723f
0093722E  BA 56 52 65 67                  mov edx, 0x67655256
00937233  48 8B CF                        mov rcx, rdi
00937236  E8 D5 94 8D FF                  call 0x140210710
0093723B  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
0093723F  48 8B C3                        mov rax, rbx
00937242  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00937247  48 83 C4 20                     add rsp, 0x20
0093724B  5F                              pop rdi
0093724C  C3                              ret
0093724D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpAllocateKeyContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(256, 48, (unsigned int)(0x67655256ULL), a4);
    if (result != 0) {
        a2 = 0x67655256ULL;
        a1 = a1;
        result = ObfReferenceObjectWithTag(a1, a2, (unsigned int)(0x67655256ULL), a4);
        *(unsigned __int64 *)(result + 40) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VrpAllocateKeyContext(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(256, 48, (uint32_t)(0x67655256ULL), a4);
    if (result != 0) {
        a2 = 0x67655256ULL;
        Arg1 = Arg1;
        result = ObfReferenceObjectWithTag(Arg1, a2, (uint32_t)(0x67655256ULL), a4);
        *(uint64_t *)(result + 0x28) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00937204&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00937204[BB_00937204]
  bb_0093722E[BB_0093722E]
  bb_0093723F[BB_0093723F]
  bb_0093724D[BB_0093724D]
  bb_00937204 -->|branch| bb_0093723F
  bb_00937204 -->|fallthrough| bb_0093722E
  bb_0093722E -->|flow| bb_0093723F
```
