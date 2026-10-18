# sub_00B1AF32

- RVA: `0x00B1AF32`–`0x00B1AF55` (길이 `35` bytes)
- VA: `0x0000000140B1AF32`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000836D0`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1AF3C` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x00B1AF46` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B1AF46` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B1AF50` → [EtwpDeleteRegistrationObject + 0x32B](../8C/EtwpDeleteRegistrationObject_function_008C1F30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1AF32  48 8B DF                        mov rbx, rdi
00B1AF35  48 8B 3F                        mov rdi, qword ptr [rdi]
00B1AF38  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B1AF3C  E8 1B 4D DA FF                  call 0x1408bfc5c
00B1AF41  33 D2                           xor edx, edx
00B1AF43  48 8B CB                        mov rcx, rbx
00B1AF46  E8 25 79 06 00                  call 0x140b82870
00B1AF4B  48 3B EF                        cmp rbp, rdi
00B1AF4E  75 E2                           jne 0x140b1af32
00B1AF50  E9 06 73 DA FF                  jmp 0x1408c225b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1AF32(__int64 a1, int a2)
{
    __int64 result;

    result = EtwpUnreferenceDataBlock(*(unsigned __int64 *)(v_rdi + 16), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, a3, a4);
    if (v_rbp != (*(unsigned __int64 *)(v_rdi))) goto loc_00B1AF32;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B1AF32(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    result = EtwpUnreferenceDataBlock(*(uint64_t *)(local_rdi + 0x10), Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, a3, a4);
    if (local_rbp != (*(uint64_t *)(local_rdi))) goto loc_00B1AF32;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1AF32&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1AF32[BB_00B1AF32]
  bb_00B1AF50[BB_00B1AF50]
  bb_00B1AF32 -->|branch| bb_00B1AF32
  bb_00B1AF32 -->|fallthrough| bb_00B1AF50
```
