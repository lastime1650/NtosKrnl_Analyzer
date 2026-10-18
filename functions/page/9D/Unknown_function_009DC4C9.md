# sub_009DC4C9

- RVA: `0x009DC4C9`–`0x009DC508` (길이 `63` bytes)
- VA: `0x00000001409DC4C9`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A36BC`
- 디코드: `11`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009DC4C9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DC4D2` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009DC4C9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC4D2` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009DC506` → [sub_009DC508 + 0x5](Unknown_function_009DC508.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009DC4C9  E8 B6 D5 1E 00                  call 0x140bc9a84
009DC4CE  48 8D 4D E7                     lea rcx, [rbp - 0x19]
009DC4D2  E8 49 D4 1E 00                  call 0x140bc9920
009DC4D7  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
009DC4DB  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
009DC4E3  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
009DC4EB  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
009DC4F3  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
009DC4FB  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
009DC503  48 85 C9                        test rcx, rcx
009DC506  74 05                           je 0x1409dc50d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009DC4C9(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28)
{
    __int64 result;

    result = CmpUnlockRegistry(a1, a2, a3, a4);
    result = CmpDetachFromRegistryProcess(v_rbp - 25, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_009DC4C9(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, int64_t Arg20, int64_t Arg21, int64_t Arg22, int64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, int64_t Arg28)
{
    int64_t result;

    result = CmpUnlockRegistry(Arg1, Arg2, Arg3, Arg4);
    result = CmpDetachFromRegistryProcess(local_rbp - 25, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DC4C9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009DC4C9[BB_009DC4C9]
```
