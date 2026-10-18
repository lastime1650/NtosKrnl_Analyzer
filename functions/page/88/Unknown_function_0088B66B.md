# sub_0088B66B

- RVA: `0x0088B66B`–`0x0088B688` (길이 `29` bytes)
- VA: `0x000000014088B66B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D268`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088B679` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0088B679` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0088B670` → [sub_0088B688 + 0x19](Unknown_function_0088B688.md) (`tail-transfer`)
  - `0x0088B683` → [AlpcMessageDestroyProcedure + 0x67](AlpcMessageDestroyProcedure_function_0088B500.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0088B66B  48 83 7B 30 00                  cmp qword ptr [rbx + 0x30], 0
0088B670  77 2F                           ja 0x14088b6a1
0088B672  8B 53 04                        mov edx, dword ptr [rbx + 4]
0088B675  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0088B679  E8 F2 71 2F 00                  call 0x140b82870
0088B67E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0088B683  E9 DF FE FF FF                  jmp 0x14088b567
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0088B66B(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;

    result = ExFreePoolWithTag(v_rdi - 48, (unsigned int)(*(unsigned int *)(v_rbx + 4)), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0088B66B(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t result;

    result = ExFreePoolWithTag(local_rdi - 48, (uint32_t)(*(uint32_t *)(local_rbx + 0x4)), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088B66B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0088B66B[BB_0088B66B]
  bb_0088B672[BB_0088B672]
  bb_0088B66B -->|fallthrough| bb_0088B672
```
