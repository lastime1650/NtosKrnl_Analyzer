# sub_006E141E

- RVA: `0x006E141E`–`0x006E1438` (길이 `26` bytes)
- VA: `0x00000001406E141E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074C4C`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E1420` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x006E142D` → [MiInsertPteTracker](../69/MiInsertPteTracker_function_00697BE4.md) (function, `0x00697BE4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E1433` → [MmMapLockedPagesSpecifyCache + 0x29A](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E141E  8B CD                           mov ecx, ebp
006E1420  E8 0B 71 BD FF                  call 0x1402b8530
006E1425  44 8B C8                        mov r9d, eax
006E1428  33 D2                           xor edx, edx
006E142A  48 8B CE                        mov rcx, rsi
006E142D  E8 B2 67 FB FF                  call 0x140697be4
006E1432  90                              nop
006E1433  E9 62 76 C3 FF                  jmp 0x140318a9a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E141E(__int64 a1, int a2)
{
    __int64 result;

    result = MiProtectionToCacheAttribute((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    a2 = 0;
    result = MiInsertPteTracker(v_rsi, a2, a3, (unsigned int)((unsigned int)(result)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E141E(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    result = MiProtectionToCacheAttribute((uint32_t)((uint32_t)(local_rbp)), Arg2, a3, a4);
    Arg2 = 0;
    result = MiInsertPteTracker(local_rsi, Arg2, a3, (uint32_t)((uint32_t)(result)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E141E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E141E[BB_006E141E]
```
