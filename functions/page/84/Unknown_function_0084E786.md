# sub_0084E786

- RVA: `0x0084E786`–`0x0084E7AE` (길이 `40` bytes)
- VA: `0x000000014084E786`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069C4C`
- 디코드: `9`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084E789` → [CmpDereferenceKeyControlBlock](../85/CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x0084E794` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0084E794` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0084E7AC` → [sub_0084E7AE + 0x5](Unknown_function_0084E7AE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0084E786  48 8B CF                        mov rcx, rdi
0084E789  E8 82 2B 00 00                  call 0x140851310
0084E78E  33 D2                           xor edx, edx
0084E790  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0084E794  E8 07 D2 BC FF                  call 0x14041b9a0
0084E799  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0084E7A1  45 84 E4                        test r12b, r12b
0084E7A4  4C 8B A4 24 08 01 00 00         mov r12, qword ptr [rsp + 0x108]
0084E7AC  74 05                           je 0x14084e7b3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0084E786(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34)
{
    __int64 result;

    result = CmpDereferenceKeyControlBlock(v_rdi, a2, a3, a4);
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_rbp - 104, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0084E786(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, int64_t Arg33, int64_t Arg34)
{
    int64_t result;

    result = CmpDereferenceKeyControlBlock(local_rdi, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(local_rbp - 104, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084E786&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084E786[BB_0084E786]
```
