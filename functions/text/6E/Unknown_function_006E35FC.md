# sub_006E35FC

- RVA: `0x006E35FC`–`0x006E362E` (길이 `50` bytes)
- VA: `0x00000001406E35FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A08C`
- 디코드: `12`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E3607` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x006E3612` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x006E361A` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E3629` → [MiAddPagesToEnclave + 0x184](../36/MiAddPagesToEnclave_function_00367EEC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E35FC  48 85 FF                        test rdi, rdi
006E35FF  74 0B                           je 0x1406e360c
006E3601  48 8B D7                        mov rdx, rdi
006E3604  48 8B CE                        mov rcx, rsi
006E3607  E8 B4 38 B3 FF                  call 0x140216ec0
006E360C  41 8A D5                        mov dl, r13b
006E360F  48 8B CE                        mov rcx, rsi
006E3612  E8 79 A0 B9 FF                  call 0x14027d690
006E3617  48 8B CE                        mov rcx, rsi
006E361A  E8 D1 95 B9 FF                  call 0x14027cbf0
006E361F  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
006E3629  E9 42 4A C8 FF                  jmp 0x140368070
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E35FC(void)
{
    __int64 result;

    if (v_rdi != 0) {
        a2 = v_rdi;
        a1 = v_rsi;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(v_rsi, (unsigned __int8)(v_r13), a3, a4);
    result = MiLockWorkingSetShared(v_rsi, (unsigned __int8)(v_r13), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E35FC(void)
{
    int64_t result;

    if (local_rdi != 0) {
        a2 = local_rdi;
        a1 = local_rsi;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(local_rsi, (uint8_t)(local_r13), a3, a4);
    result = MiLockWorkingSetShared(local_rsi, (uint8_t)(local_r13), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E35FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E35FC[BB_006E35FC]
  bb_006E3601[BB_006E3601]
  bb_006E360C[BB_006E360C]
  bb_006E35FC -->|branch| bb_006E360C
  bb_006E35FC -->|fallthrough| bb_006E3601
  bb_006E3601 -->|flow| bb_006E360C
```
